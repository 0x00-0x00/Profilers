#!/usr/bin/env python
import os
def validate_day(day):
    if(int(day) < 32):
        return True
    else:
        return False

def validate_month(month):
    if(int(month) < 13):
        return True
    else:
        return False

def validate_year(year, target_year):
    if(int(year) <= int(target_year)):
        return True
    else:
        return False


class Date(object):
    def __init__(self, day, month, year, target_year, output_file):
        d=self.generate(day,month,year,target_year)
        with open(output_file, "w") as f:
            for i in d:
                f.write(i + "\n")

    def generate(self, day,month,year,target_year):
        l=[]
        while validate_year(year, target_year):
            if(validate_month(month)):
                if(validate_day(day)):
                    d=str(day).zfill(2) + str(month).zfill(2) + str(year).zfill(4)
                    l.append(d)
                    d=str(day).zfill(2) + str(month).zfill(2) + str(year)[2:]
                    l.append(d)
                    day+=1
                else:
                    month+=1
                    day=1
            else:
                year+=1
                month=1
        return l


print "Date Wordlist Generator written by n3st0r"
y1=int(raw_input("Type the year to begin with .....: "))
y2=int(raw_input("Type the year to finish with ....: "))
of=str(raw_input("Type the output file name .......: "))
d=Date(1,1,y1,y2,of)
if(os.path.isfile(of)):
    print "Wordlist generated and stored as %s." % (of)
else:
    print "Wordlist file could not be generated."
