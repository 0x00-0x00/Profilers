#coding:utf-8
#Script to generate numeric mnemonic combinations useful to password cracking
#when the scenario presents low digit numeric passwords.

output = []
numer=[1,2,3,4,5,6,7,8,9,0]
for a in range(1,6):
    for i in numer:
        for u in numer:
            output.append(str(i) * a + str(u) * a)

for a in range(1,4):
    for i in numer:
        for u in numer:
            for y in numer:
                output.append(str(i) * a + str(u) * a + str(y) * a)

for a in range(1,3):
    for i in numer:
        for u in numer:
            for y in numer:
                for t in numer:
                    output.append(str(i) * a + str(u) * a + str(y) * a + str(t) * a)
print output
print "Output has %d elements." % (len(output))
file_name = str(raw_input("Output file: "))
with open(file_name,"w") as f:
    for element in output:
        f.write(element + "\n")
print "Output sent to file %s." % (file_name)
