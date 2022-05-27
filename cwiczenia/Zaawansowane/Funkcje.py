import random
filer = open("obraz.bmp")
def kopiuj():
    filer = open("rts.bmp")
    filew = open(str(random.randint(1, 1000)) + ".bmp", "w")
    filew.write(filer.read())
    filer.close()
    filew.close()
'''
for x in range(0, 5):
    kopiuj()
'''

print(filer.read())