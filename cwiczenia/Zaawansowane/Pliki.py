import random

plik1 = open("n.txt", "r")
plik2 = open("n-copy.txt", "w")
text1 = plik1.read()

pisz = True

for x in text1:
    if pisz:
        plik2.write(x)
        pisz = False
    else:
        pisz = True

plik1.close()
plik2.close()
