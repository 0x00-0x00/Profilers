#!/usr/bin/python
# coding: utf-8

# PPP - Personal Password Profiling
# ----------------------------------
# Program written to modulate words into accurate used passwords to help with dictionary attacks.
# This program is probably better to be used with Portuguese-BR language words.
# Author: zc00l


import itertools


def all_combinations(s):
    """
    Return alls the possible combinations for N-length given a set of N length.
    :param s:
    :return: list with all possible combinations of given set.
    """
    if type(s) is not list:
        return None
    n = len(s)
    output = list()
    x = itertools.product(s, repeat=n)
    try:
        while True:
            output.append(''.join(x.next()))
    except StopIteration:
        return output


def l33t(string, a, b):
    return str(string).replace(a, b)


def reverse(string):
    return string[::-1]


def name_scrambler(string):
    # turn to lower
    string = str(string.lower())

    # get names splitting the space character
    names = string.split(" ")

    # creates the output list
    output = []

    # banned words
    banned = ["de", "da", "do", "dos", "das"]

    #  Gets initial letters from all names
    initial_letters = str()
    if len(names) > 1:
        for name in names:
            if name not in banned:
                initial_letters += str(name[0:1]).lower()

        # Pega as duas iniciais e insere na lista names
        if len(initial_letters) > 1:
            names.append(str(initial_letters)[0:2])

        # algoritmo para pegar todas combinações possíveis com os nomes
        # Generate all names combinations possible
        for name in names:
            for surname in names:
                if name != surname and surname not in banned and name not in banned:
                    output.append(str(name) + str(surname))
                    output.append(alpha_case(name) + str(surname))
                    output.append(alpha_case(name) + alpha_case(surname))
                    output.append(up_and_down(str(name) + str(surname)))
                    output.append(up_and_down(str(name) + str(surname), i=1))
                    output.append(str(name).upper() + str(surname).upper())

    # First name and variations
    # Primeiro nome e variacoes
    output.append(str(names[0]).upper())
    output.append(str(names[0]).lower())
    output.append(reverse(str(names[0]).lower()))
    output.append(reverse(str(names[0]).upper()))
    output.append(alpha_case(str(names[0]).lower()))
    output.append(up_and_down(str(names[0]).lower()))
    output.append(up_and_down(str(names[0]).lower(), i=1))

    # First name and variations with only 3 first characters
    # Primeiro nome e variacoes com somente os 3 primeiros caracteres
    output.append(str(names[0][0:3]).upper())
    output.append(str(names[0][0:3]).lower())
    output.append(alpha_case(str(names[0][0:3]).lower()))
    output.append(up_and_down(str(names[0][0:3]).lower()))
    output.append(up_and_down(str(names[0][0:3]).lower(), i=1))

    # First name and variations with only 2 first characters
    # Primeiro nome e variacoes com apenas 2 primeiros caracteres
    output.append(str(names[0][0:2]).upper())
    output.append(str(names[0][0:2]).lower())
    output.append(alpha_case(str(names[0][0:2]).lower()))
    output.append(up_and_down(str(names[0][0:2]).lower()))
    output.append(up_and_down(str(names[0][0:2]).lower(), i=1))

    # Primeiro e ultimo e variacoes
    # First and last name variations
    output.append(str(names[0] + names[len(names) - 1]).upper())
    output.append(str(names[0] + names[len(names) - 1]).lower())
    output.append(alpha_case(str(names[0] + names[len(names) - 1]).lower()))
    output.append(up_and_down(str(names[0][0:3]).lower()))
    output.append(up_and_down(str(names[0][0:3]).lower(), i=1))

    if len(names) > 1:
        # primeiras letras em minusculo
        if initial_letters != "":
            output.append(str(initial_letters).lower())
            output.append(str(initial_letters).upper())
        output.append(reverse(str(initial_letters).upper()))
        output.append(reverse(str(initial_letters).lower()))
        output.append(alpha_case(str(initial_letters)))
        output.append(up_and_down(str(initial_letters)))
        output.append(up_and_down(str(initial_letters), i=1))

    # leetificar tudo
    leet = []
    # leets = {"a": "4", "e": "3", "o": "0", "l": "1"}
    # for variation in output:

    for combination in output:
        # This could be enhanced using nested loops
        leet_output = l33t(combination, "a", "4")
        leet_output = l33t(leet_output, "e", "3")
        leet_output = l33t(leet_output, "o", "0")
        leet_output = l33t(leet_output, "l", "1")
        leet.append(leet_output)

    # adiciona o l33t na lista final
    for l in leet:
        # f.append(l) LEET DESABILITADO - DESCOMMENT PARA HABILITAR
        pass

    return output


def detect_date(date):
    if len(date) == 6:
        four_digits = str("20" + str(date[-2:]))
        if int(four_digits) > 2017:
            return [date, date[0:4] + "19" + date[4:], date[0:2] + date[3:4] + date[4:],
                    date[0:2] + date[3:4] + "19" + date[4:]]
        else:
            return [date, date[0:4] + "19" + date[4:], date[0:4] + "20" + date[4:], date[0:2] + date[3:4] + date[4:],
                    date[0:2] + date[3:4] + "20" + date[4:], date[0:2] + date[3:4] + "19" + date[4:]]
    else:
        return [date, date[0:4] + date[6:], date[0:2] + date[3:4] + date[-2:], date[0:2] + date[3:4] + date[4:]]


def relation_person_date(person, date):
    buff = []
    for element in detect_date(date):
        buff.append(str(person) + str(element))
    return buff


def has_integer(string):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if type(string) is int:
        return True
    if type(string) is float:
        return True
    if type(string) is str:
        for char in string:
            if char in numbers:
                return True
    return False


def up_and_down(string, i=0):
    i = i
    output = str()
    for character in string:
        if i % 2 != 0:
            output += character.upper()
        else:
            output += character.lower()
        i += 1
    return output


def alpha_case(string):
    return str(string)[0:1].upper() + str(string)[1:].lower()


def generate_years(b, n=50):
    """
    Process of refactoration of 08 Jan 2017
    Refactoring process_data function with smaller functions
    :param b: Current year integer number
    :param n: Number of years to roll back
    :return: string list
    """
    output = list()
    for x in range(b - n, b, 1):
        output.append("{0}".format(x))
        output.append("_{0}".format(x))
    return output


def process_data(wl, output_file):
    print "\n---------------------\nResultados: \n"
    output_list = list()

    # Lista DS usada para estabelecer sufixos definidos como ultimos 8 anos e 123 e 321
    ds4 = ["_123", "_321"]
    ds3 = ["123", "321", "111", "222", ]
    ds2 = ["11", "22", "01", "02", "03"]
    dyn_specials = ["*", "%", "!", "#"]
    ds = [dyn_specials, ds2, ds3, ds4]

    # Hardcore mode
    # ds2 = all_combinations(["0", "1", "2", "3"])
    # ds = [dyn_specials, ds2]

    # Refactored this in 08 Jan 2017
    # adiciona anos para a lista ds
    # while pano < ano:
    #    ds2.append(str(pano))
    #    ds2.append(str("_%s" % str(pano)))
    #    pano += 1
    # ano = 2018
    # for x in range(ano - 50, ano, 1):
    #     ds2.append("{0}".format(x))
    #     ds2.append("_{0}".format(x))

    ds2.extend(generate_years(2018, 50))

    for key in wl:
        cel = wl["celular"]
        tel = wl["telefone"]
        bd = []
        if key == "nome":
            word = wl[key]
            for nome in name_scrambler(word):
                if has_integer(nome) is False:
                    output_list.append(nome)
                    # New code:
                    [[output_list.append(str(nome) + str(y)) for y in x] for x in ds]
                    # Refactoration of 08 Jan 2017
                    # Past code:
                    # for l in ds:
                    #     for i in l:
                    #         output_list.append(str(nome) + str(i))

            if wl["palavras-chave"] is not "":
                word = wl["palavras-chave"]
                word = str(word).replace(' ', '')
                d = word.split(',')
                a = str()
                for i in d:
                    a += i + " "
                for nome in name_scrambler(a):
                    if has_integer(nome) is False:
                        output_list.append(nome)

                        # New code:
                        [[output_list.append(y) for y in x] for x in ds]
                        # Refactoration of 08 Jan 2017
                        # Past code:
                        # for l in ds:
                        #    for z in l:
                        #        output_list.append(str(nome) + str(z))

            if wl["aniversario"] is not "":
                bdf = list()
                bday = wl["aniversario"]
                bd = detect_date(bday)
                # gera as possiveis datas de aniversario em formato 6 e 8
                for date in bd:
                    # pega as senhas ja geradas pelo nome e adiciona a string da data no final em uma lista separada bdf
                    for element in output_list:
                        if (element[-1:] not in dyn_specials and element[-2:] not in ds2 and element[-3:] not in ds3 and element[
                                                                                                                -4:] not in ds4):
                            bdf.append(element + date)
                            bdf.append(element + "_" + date)
                            for special in dyn_specials:
                                bdf.append(element + date + special)
                                bdf.append(element + "_" + date + special)
                # adiciona na lista OuputList todo o conteudo da lista bdf
                for element in bdf:
                    output_list.append(element)

            if wl["celular"] is not "" or wl["telefone"] is not "":
                bdc = []
                for element in output_list:
                    if element[-1:] not in dyn_specials and element[-2:] not in ds2 and element[-3:] not in ds3 \
                            and element[-4:] not in ds4:
                        d = False
                        for date in bd:
                            if date in element:
                                d = True
                                break
                            else:
                                d = False
                        if d is False:
                            if cel is not "":
                                bdc.append(element + cel)
                            if tel is not "":
                                bdc.append(element + tel)
                                if len(tel) > 4:
                                    # adiciona os 4 digitos do telefone no elemento
                                    bdc.append(element + str(tel)[0:4])

                # adiciona na lista OuputList todo o conteudo da lista bdf
                for element in bdc:
                    output_list.append(element)

            three_last_digits = []
            for element in output_list:
                met = True
                for list_unit in ds:
                    for banned_string in list_unit:
                        if banned_string in element:
                            # print "Element %s does not meet requirements for numerical addition because it contains
                            #  %s." % (element, banned_string)
                            met = False
                            break
                for date in bd:
                    if date in element:
                        # print "Element %s does not meet requirements for numerical addition because it contains
                        # %s." % (element, date)
                        met = False
                        break
                if met is True:
                    # print "Element %s meets the requirement." % (element)
                    three_last_digits.append(element + "1")
                    three_last_digits.append(element + "2")
                    three_last_digits.append(element + "3")
            for i in three_last_digits:
                output_list.append(i)

            for date in bd:
                output_list.append(date)
            if cel is not "":
                output_list.append(cel)
            if tel is not "":
                output_list.append(tel)

    output_list = list(set(output_list))
    print "Foram geradas %d senhas." % (len(output_list))
    # ofile = raw_input("Name of file to output:")
    with open(output_file, "w") as f:
        for element in output_list:
            f.write(element + "\n")
    print "Senhas salvas em %s" % str(ofile)
    return len(output_list)


def get_input():
    print "--------------------------------"
    print "::: Coleta de Dados Pessoais :::"
    print "--------------------------------"
    n = raw_input("Digite o nome: ...........: ")
    b = raw_input("Digite o aniversario .....: ")
    c = raw_input("Digite o celular .........: ")
    t = raw_input("Digite o telefone fixo....: ")
    d = raw_input("Digite palavras extras ...: ")
    print "--------------------------------"
    w = int(raw_input("Ativar [Módulo Wireless] .: "))
    e = int(raw_input("Ativar [Módulo E-mail] ...:"))
    return {"nome": n, "aniversario": b, "celular": c, "telefone": t, "palavras-chave": d, "wireless": w, "email": e}


# def main():
#    wl = get_input()
#    process_data(wl)


# if __name__ == "__main__":
#    main()
