#coding:utf-8

pmin = int(raw_input("Passwords per min ....: "))
pnum = int(raw_input("Passwords to run .....: "))

minutes = pnum/pmin

def print_result(m):
    if(m > 60):
        h=(m/60)
        if(h>24):
            d=(h/24)
            return "O crack terminará em %.2f dias." % (float(d))
        return "O crack terminará em %.2f horas." % (float(h))

    else:
        return "O crack terminará em %.2f minutos." % (float(m))


print print_result(minutes)
