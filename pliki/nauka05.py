f = open("uczniowie.txt", "r", encoding="UTF-8")

jedna_linia = f.readline()
print(jedna_linia)

# wczytaj wszystkie linie do końca
linie = f.readlines()
print(linie)
