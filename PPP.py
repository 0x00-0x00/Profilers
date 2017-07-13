#!/usr/bin/python
#coding: utf-8

#PPP - Personal Password Profiling
#----------------------------------
#Author: n3st0r

def l33t(string, a, b):
	return str(string).replace(a, b)

def reverse(string):
	l=len(string)
	s=""
	i=1
	for char in string:
		s+=string[l-i:l]
		l-=1
	return s

def name_scrambler(string):
	#transforma a string em lower
	string=str(string.lower())

	#divide o nome em uma lista separada pelos espaços
	d=string.split(" ")

	#cria a lista final
	f=[]
 
        for _ in d:
            f.append(_.lower())
            f.append(_.upper())
            f.append(_[0:1].upper() + _[1:].lower())



	#lista de palavras banidas
	banned = ["de", "da", "do", "dos", "das"]

	#algoritmo para pegar as primeiras letras do nome
	if(len(d) > 1):
		primeiras_letras = ""
		for i in d:
			if(i not in banned):
				primeiras_letras+=str(i[0:1]).lower()

	#pega as primeiras letras dos dois primeiros nomes
		d.append(str(primeiras_letras)[0:2])


	#algoritmo para pegar todas combinações possíveis com os nomes
		for i in d:
			for a in d:
				if(i !=a and a not in banned and i not in banned):

					f.append(str(i) + str(a))
					f.append(AlphaCase(i) + str(a))
					f.append(AlphaCase(i) + AlphaCase(a))
					f.append(UpAndDown(str(i) + str(a)))
					f.append(str(i).upper() + str(a).upper())

	#primeiro nome em minusculo
	f.append(str(d[0]).upper())
	f.append(str(d[0]).lower())
	f.append(reverse(str(d[0]).lower()))
	f.append(AlphaCase(str(d[0]).lower()))
	f.append(UpAndDown(str(d[0]).lower()))

	#primeiro nome apenas 3 primeiros digitos
	f.append(str(d[0][0:3]).upper())
	f.append(str(d[0][0:3]).lower())
	f.append(AlphaCase(str(d[0][0:3]).lower()))
	f.append(UpAndDown(str(d[0][0:3]).lower()))

	#primeiro nome apenas 2 primeiros digitos
	f.append(str(d[0][0:2]).upper())
	f.append(str(d[0][0:2]).lower())
	f.append(AlphaCase(str(d[0][0:2]).lower()))
	f.append(UpAndDown(str(d[0][0:2]).lower()))

	#primeiro e ultimo nome em minusculo
	f.append(str(d[0] + d[len(d)-1]).upper())
	f.append(str(d[0] + d[len(d)-1]).lower())
	f.append(AlphaCase(str(d[0] + d[len(d)-1]).lower()))
	f.append(UpAndDown(str(d[0][0:3]).lower()))

	if(len(d) > 1):
		#primeiras letras em minusculo
		f.append(str(primeiras_letras))
		f.append(str(primeiras_letras).upper())
		f.append(AlphaCase(str(primeiras_letras)))
		f.append(UpAndDown(str(primeiras_letras)))





	#leetificar tudo
	leet=[]
	for combination in f:
		output=l33t(combination, "a", "4")
		output=l33t(output, "e", "3")
		output=l33t(output, "o", "0")
		output=l33t(output, "l", "1")
		leet.append(output)



	#adiciona o l33t na lista final
	for l in leet:
		#f.append(l) LEET DESABILITADO - DESCOMMENT PARA HABILITAR
		pass



	return f

def detect_date(date):
	if(len(date) == 6):
		fourD= str("20" +  str(date[-2:]))
		if(int(fourD) > 2017):
			return [date, date[0:4] + "19" + date[4:], date[0:2] + date[3:4] + date[4:], date[0:2] + date[3:4] + "19" + date[4:]]
		else:
			return [date, date[0:4] + "19" + date[4:], date[0:4] + "20" + date[4:] , date[0:2] + date[3:4] + date[4:], date[0:2] + date[3:4] + "20" +  date[4:], date[0:2] + date[3:4] + "19" + date[4:]]
	else:
		return [date, date[0:4] + date[6:], date[0:2] + date[3:4] + date[-2:], date[0:2] + date[3:4] + date[4:]]

def relation_person_date(person, date):
	buff=[]
	for element in detect_date(date):
		buff.append(str(person) + str(element))
	return buff

def integral_digit(string):
	if(type(string) == str):
		for char in string:
			try:
				char = int(char)
			except:
				return False
		return True
	else:
		return True

def UpAndDown(string):
	i=0
	fc=""
	l=len(string)
	while(i<(l+1)):
		if(i % 2 == 0):
			fc+= str(string)[i:(i+1)].upper()
		else:
			fc+= str(string)[i:(i+1)].lower()
		i+=1
	return fc

def AlphaCase(string):
	return str(string)[0:1].upper() + str(string)[1:].lower()

def process_data(wl):
	print "\n---------------------\nResultados: \n"
	oL=[]
	#Lista DS usada para estabelecer sufixos definidos como ultimos 8 anos e 123 e 321
	ds4=["_123", "_321"]
	ds3=["123","321", "111",  "222",]
	ds2=["11","22","01","02","03"]
	dsS=["*","%","!","#"]
	ds=[dsS, ds2, ds3, ds4]
	#Variavel para proximo ano
	ano=2017

	#variavel para diminuir 8 anos do atual ano
	pano= ano - 8

	#adiciona anos para a lista ds
	while(pano < ano):
		ds4.append(str(pano))
		ds4.append(str("_%s" % str(pano)))
		pano+=1


	for key in wl:
		cel=wl["celular"]
		tel=wl["telefone"]
		bd=[]
		if(key == "nome"):
			word = wl[key]
			for nome in name_scrambler(word):
				if(integral_digit(nome) == False):
					oL.append(nome)

					for l in ds:
						for i in l:
							oL.append(str(nome) + str(i))

			if(wl["palavras-chave"] is not ""):
				word = wl["palavras-chave"]
				word=str(word).replace(' ','')
				d=word.split(',')
				a=""
				for i in d:
					a+= i + " "
				for nome in name_scrambler(a):
					if(integral_digit(nome) == False):
						oL.append(nome)
						for l in ds:
							for z in l:
								oL.append(str(nome) + str(z))
			if(wl["aniversario"] is not ""):

				bdf=[]
				bday=wl["aniversario"]
				bd=detect_date(bday)
				#gera as possiveis datas de aniversario em formato 6 e 8
				for date in bd:
					#pega as senhas ja geradas pelo nome e adiciona a string da data no final em uma lista separada bdf
					for element in oL:
						if(element [-1:] not in dsS and element[-2:] not in ds2 and element[-3:] not in ds3 and element[-4:] not in ds4):
							bdf.append(element + date)
							bdf.append(element + "_" + date)
							for special in dsS:
								bdf.append(element + date + special)
								bdf.append(element + "_" + date + special)
				#adiciona na lista OuputList todo o conteudo da lista bdf
				for element in bdf:
					oL.append(element)
			if(wl["celular"] is not "" or wl["telefone"] is not ""):
				bdc=[]


				for element in oL:
					if element[-1:] not in dsS and element[-2:] not in ds2 and element[-3:] not in ds3 and element[-4:] not in ds4:
						d=False
						for date in bd:
							if date in element:
								d=True
								break
							else:
								d=False
						if d is False:
							if cel is not "":
								bdc.append(element + cel)
							if tel is not "":
								bdc.append(element + tel)
								if len(tel) > 4:
									#adiciona os 4 digitos do telefone no elemento
									bdc.append(element + str(tel)[0:4])

				#adiciona na lista OuputList todo o conteudo da lista bdf
				for element in bdc:
					oL.append(element)

			three_last_digits = []
			for element in oL:
				met=True
				for list_unit in ds:
					for banned_string in list_unit:
						if banned_string in element:
							#print "Element %s does not meet requirements for numerical addition because it contains %s." % (element, banned_string)
							met=False
							break
				for date in bd:
					if date in element:
						#print "Element %s does not meet requirements for numerical addition because it contains %s." % (element, date)
						met=False
						break
				if met is True:

					#print "Element %s meets the requirement." % (element)
					#p=raw_input("Press Anything to Move On...")
					three_last_digits.append(element + "1")
					three_last_digits.append(element + "2")
					three_last_digits.append(element + "3")
			for i in three_last_digits:
				oL.append(i)

			for date in bd:
				oL.append(date)
			if(cel is not ""):
				oL.append(cel)
			if(tel is not ""):
				oL.append(tel)







	oL=list(set(oL))
	print "Foram geradas %d senhas." % (len(oL))
	ofile=raw_input("Name of file to output:")
	with open(ofile, "w") as f:
		for element in oL:
			f.write(element + "\n")
	print "Senhas salvas em %s" % str(ofile)



def get_input():

	print "--------------------------------"
	print "::: Coleta de Dados Pessoais :::"
	print "--------------------------------"
	n=raw_input("Digite o nome: ...........: ")
	b=raw_input("Digite o aniversario .....: ")
	c=raw_input("Digite o celular .........: ")
	t=raw_input("Digite o telefone fixo....: ")
	d=raw_input("Digite palavras extras ...: ")
	print "--------------------------------"
	w=int(raw_input("Ativar [Módulo Wireless] .: "))
	e=int(raw_input("Ativar [Módulo E-mail] ...:"))
	return {"nome":n,"aniversario":b,"celular":c,"telefone":t,"palavras-chave":d, "wireless":w,"email":e}

def main():
	wl = get_input()
	process_data(wl)

if __name__ == "__main__":
	main()
