#coding:utf-8


def generate_all_possibilites(base,list):
    for i in range(0,10000):
        #adiciona na lista recebida pela função o elemento da base + todas as combinacoes de numeros de 0-9999
        list.append(str(base) + str(i).zfill(4))
    return

#99600
min_base = int(raw_input("Type the minimum base: "))
#99899
max_base = int(raw_input("Type the maximum base: "))


output = []
base_list = []

#Adiciona a faixa de números BASES (ex: 99633 - 99870 ) dos pretensos números para uma lista
while min_base < max_base:
    base_list.append(min_base)
    min_base+=1

for base in base_list:
    generate_all_possibilites(base, output)

print output
print "Output has %d elements." % (len(output))
