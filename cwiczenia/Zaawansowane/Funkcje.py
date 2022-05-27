import random

'''Kopiowanie plików

def kopiuj():
    filer = open("rts.bmp")
    filew = open(str(random.randint(1, 1000)) + ".bmp", "w")
    filew.write(filer.read())
    filer.close()
    filew.close()

for x in range(0, 5):
    kopiuj()
'''

def pot(a ,b):
    wynik = 1
    for x in range(0, b):
        wynik *= a
    print(wynik)

pot(2,3)