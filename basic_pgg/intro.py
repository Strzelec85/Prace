# to jest komentarz jednolinijkowy
# Uruchomienie na Macu: ctrl+shift+r
# Uruchomienie na Windowsie: ctrl+shift+f10
print("Hello world!")

# Typy danych
# napis, string - str
# definiujemy w " albo '
print('Hello world!')
print("Hello world!")

print("Ksiazka 'Pan Tadeusz' jest fajna!")
print('Ksiazka "Pan Tadeusz" jest fajna')
print("Ksiazka \"Pan Tadeusz\" jest fajna") # trzeba wyeskejpowac \"
print('Ksiazka \'Pan Tadeusz\' jest fajna')

# int - liczby całkowite
# int - ma nieograniczoną precyzje
print(10)

# float
print(3.14)
print(3.0)
print(3.)
print(0.5)
print(.5)

print(type(3.0)) # float
print(type(3)) # int

print(type(float(3))) # zmiana typu / rzutowanie

# bool
# typ danych, który posiada dwie wartości: prawda i fałsz
print(True)
print(False)

print(type(True))
print(type(False))

# wartość pusta
# w innych językach zwykle jest to null
print(None)

print(type(10)) # int
print(type(10.0)) # float
print(type("10")) # str

print(10 + 5) # 15
print("10" + "5") # 105 - tekst a nie liczba!

# Operatory
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5) # int / int -> float!
print(10 // 3) # dzielenie calkowitoliczbowe
print(type(10 // 3)) # dzielenie calkowitoliczbowe, dostajemy int
print(10 % 3) # reszta z dzielenia, modulo
print(10 ** 3) # potegowanie

print("Ala " + "ma kota") # konkatenacja, laczenie napisow
print("Ala" * 10) # powielamy napis X razy


# print("Ala ma lat: " + 10) # nie zadziala i bedzie blad
print("Ala ma lat: " + str(10)) # przerabiasz int na string
print("Ala ma lat: " + str(10.5))

# literal - wartosc wpisana bezposrednio w kodzie

# żąśźćęńłó - w komentarzach mogą być polskie znaki

print('Ala ma kota')
print("Ala ma\nkota")
print("""Ala ma kota
Kot ma kompilator
jest nowy wiersz""")

print('''Pierwsza linijka
Druga linijka
Trzecia linijka
''')

# zmienna
imie = 'Piotr' # nazwa_zmiennej = wartosc

print(imie)

imie = 44

print(imie)

imie = "Tomek"
print(imie)

# PEP - Python Enhancements Proposal
# PEP8 - style guide
# nazywanie zmiennych: PEP8 https://www.python.org/dev/peps/pep-0008

adres_zamieszkania = "ul. Polna 10, 12-345 Warszawa"

napis_z_polskimi_znakami = "Zażółć gęślą jaźń"
print(napis_z_polskimi_znakami)

print('-' * 30)

# format specifiers
# https://www.python.org/dev/peps/pep-0498/#format-specifiers
# https://docs.python.org/3.4/library/string.html#formatspec

waga = 123.456
print(f"Waga: {waga}")
print(f"Waga: |{waga:_^10.2f}|")

moj_napis = f"Waga: |{waga:_^10.2f}|"
print(moj_napis)

print('-'*30)

############################################################

# Python jest językiem słabo typowanym (weakly types)
# w przeciwienstwie do jezykow scisle typowanych (strongly typed) jak np. Java

imie = "Piotr"
print(imie)

imie = 44.444
print(imie)

imie = 44
print(imie)

############################################################
print('-'*30)

liczba = 10
print(liczba)

liczba = liczba + 5
print(liczba) # -> 15

# = -> to jest przypisania

wiek = 10
wiek += 5 # to jest rownowazne wiek = wiek + 5
print(wiek)
wiek -= 5
wiek *= 5
wiek /= 5
wiek //= 5

# w jezykach takicj jak PHP, Java, C#
# mozna zamiast liczba += 1 napisac liczba++
wiek2 = 10
wiek2 **= 2
print(wiek2)

wiek3 = 10
wiek3 %= 3
print(wiek3)

############################################################
print('-'*30)

# Operatory porównania
print(1 == 1) # zeby sie niepomylic: porownanie == a przypisanie =
print(1 != 1) # rozne od
print(1 < 2) # True
print(1 > 2) # False
print(1 > 1) # False
print(1 < 1) # False
print(1 <= 1) # True
print(1 >= 1) # True

# takie porownywanie nie za bardzo jest przydatne
print('a' < 'b') # True
print('c' < 'b') # False

print('ala' == 'ala') # True
print('ala' == 'Ala') # False
print('ala ' == 'ala') # False
print('ala' != 'krysia') # True

print('Alibaba' < 'Alibac') # True

print('-'*30)

########################################################################
# instrukcje warunkowe

# liczba = int(input("Podaj liczbe: "))
liczba = 10
print(liczba)
print("jestem przed ifem")

if liczba == 10:
    print("Jestem w if")
    print("Brawo! Wygrales!! Podales liczbe 10")
elif liczba == 20:
    print("Jestem w elif")
    print('Hoho! Podales 20!')
elif liczba == 30:
    print("Jestem w elif 2")
    print('Hoho! Podales 30!')
else:
    print("Jestem w else")
    print("Niestety nie wygrales")

print("Jestem poza ifem")
print("Papa")


print('-'*30)

# liczba = int(input('Podaj liczbe: '))
liczba = 10

# czy jest z zakresu od 0 do 10
if liczba >= 0 and liczba <= 10:
    print("Liczba od 0 do 10!!!")
else:
    print("Liczba spoza zakresu!")


if 0 <= liczba <= 10:
    print("Liczba od 0 do 10!!!")
else:
    print("Liczba spoza zakresu!")


print('-'*30)
########################################################################

# Petle
# while

i = 0
while i < 100:
    print(i)
    i += 1

print("Jestem poza petla")

print('-'*30)
########################################################################

while True:
    # liczba = int(input("Podaj liczbe: "))
    liczba = 6
    print(f'Twoja liczba to {liczba}')

    if liczba % 2 == 0:
        print("Podales liczbe parzysta, konczymy petle")
        break

print('Jestem poza petla while')

print('-'*30)
########################################################################












