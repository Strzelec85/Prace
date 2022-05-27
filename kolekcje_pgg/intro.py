# Kolekcje

# Tupla, krotka, tuple

#    0   1   2 - indeks

a = (10, 20, 30)
print(a)
print( a[1] ) # 20
print( a[0] ) # 10

print('-'*30)

#    0  1    2              3 - indeks
b = (1, 2.5, "Ala ma kota", True)
print(b[0])
print(b[1])
print(b[2])
print(b[3])

# b[0] = 100 # TypeError: 'tuple' object does not support item assignment

#     0       1                2
c = ( (1, 2), ('a', 'b', 'c'), (True, False) )
#      0  1    0    1    2      0     1

print(c[0][1])
print(c[1][2])

print(type(c)) # tuple
print('-'*30)

# jak stworzyć tuple, ktora ma tylko jeden element?
d = (100,) # to , a nie nawiasy powoduja, ze python tworzy tuple!
print(type(d))

print('-'*30)

#          0    1    2    3    4    5    6    7    8
literki = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')

print(literki[0])
print(literki[3])
# [a:b] - lewostronnie domkniety, prawostronnie otwarty
print(literki[1:3]) # b, c
print(literki[1:9]) # 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'
print(literki[3:]) # 'd', 'e', 'f', 'g', 'h', 'i'
print(literki[-1]) # 'i'
print(literki[-3:]) # 'g', 'h', 'i'
print(literki[-3:-2]) # g
print(literki[5:-2]) # f, g - bo ostatni nie wchodzi!
print(literki[:-1]) # 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
print(literki[:])
print(literki[-2:3]) # pusta tupla
# od : do : co ile
print(literki[::2]) # co drugi element, 'a', 'c', 'e', 'g', 'i'
print(literki[::-1]) # 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'

print('-'*30)

# ile tupla ma elementow?
print(len(literki))

# czy element znajduje sie w tupli
print('a' in literki)

liczby = (10, 20, 30, 40, 50)

print(max(liczby))
print(min(liczby))
print(sum(liczby))

i = (1, 2, 3)
j = (4, 5, 6)

k = i + j
print(k)

l = i * 5
print(l)

print('-'*30)
###################################################
# Listy

liczby = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(type(liczby))

# operator [] (dostępu, wycinania) działa dokładnie tak samo jak w tupli

liczby[0] = 11 # operator przypisania działa w listach
print(liczby)

# liczby[10] = 110 # IndexError: list assignment index out of range

liczby.append(110) # doklada element na koniec listy
print(liczby)
print(liczby[10])

liczby.insert(1, 12) # wstawia 12 na indeks 1, pozostale elementy przesuwa
print(liczby)

liczby[0:2] = [1, 2]
print(liczby)

liczby[0:2] = [1, 2, 3]
print(liczby)

liczby.extend([111, 222, 333]) # dopisuje elementy na koncu listy
print(liczby)

# do usuwania elementow z listy uzywamy funkcji del()
# i dodatkowo operatora dostępu
del(liczby[0])
print(liczby)
print(liczby[0])

del(liczby[1:4])
print(liczby)

print('-'*30)

# sortowanie
literki = ['z', 'r', 'a', 'c']
print(literki)
literki.sort()
print(literki)

print('-' * 30)

# Petla for

liczby = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 0
while i < len(liczby):
    print(f'Element listy: {liczby[i]}')
    i += 1

print('-' * 30)

for x in liczby:
    print(f'Element listy: {x}')

print('-' * 30)

# Funckja range()
# range(do) - prawostronnie otwarta
# range(od, do) - lewostronnie zamknięta, prawostronnie otwary
# range(od, do, co_ile) - lewostronnie zamknięta, prawostronnie otwarty z krokiem co_ile

for i in range(10):
    print(i)

print('-' * 30)

for i in range(-10, 10):
    print(i)

print('-' * 30)

for i in range(-10, 10, 2):
    print(i)

print('-' * 30)

# Petla for z dostepem do indeksu i wartosci

imiona = ['Ala', 'Krysia', 'Tomek', 'Piotr']

# klucz, wartosc
# nazwy zmiennych tymczasowych moga byc dowolne
for indeks, imie in enumerate(imiona):
    print(f'indeks={indeks}, imie={imie}')

print('-' * 30)

# Zamien wartosci w zmiennych miejscami
a = 10
b = 20
print(a, b)

# z uzyciem zmiennej dodatkowej
kopia_a = a
a = b
b = kopia_a

print(a, b) # 20, 10

print('-' * 30)

a = 10
b = 20

print(a, b)

a, b = b, a

print(a, b)

print('-' * 30)

# Napisy

napis = "Ala ma kota a kot ma kompilator"
print(napis)
print(napis[0])
print(napis[1:3])
print(napis[::-1])

# wszystkie dzialania zwiazane z operatorem dostepu/wycinania
# jak w listach i tuplach sa rowniez dostepne w napisach (stringach)

print(napis.lower())
print(napis.upper())
print(napis.title())
print(napis.capitalize())

# dzielenie napisu
print(napis.split())
print(napis.split(' '))
print(napis.split('a'))

print('-' * 30)

# laczenie napisow jakims znakiem
podzielony_napis = napis.split(' ')
print(podzielony_napis)

po_scaleniu = '<->'.join(podzielony_napis)
print(po_scaleniu)

print('-' * 30)

print(napis.count('a')) # zlicza wystapienia znaku w napisie
print(napis.index('a')) # indeks pierwszego wystapienia napisu
print(napis.find('a')) # indeks pierwszego wystapienia napisu

# czym sie rozni index od find?
# print(napis.index('z')) # rzuca wyjatek kiedy nie znajdzie przekazanego ciagu znakow w orginalnym napisie
print(napis.find('z')) # jak nie znajdzie, to zwraca -1

print(napis.replace('a', '*'))
print(napis.replace('kot', '******'))

print('-' * 30)

# Slownik, dictionary, dict

slownik = {
    'imie': 'Piotr',
    'nazwisko': 'GG',
    'wiek': 18,
    'czy_pelnoletni': True,
    'ulubione_ksiazki': ['Pan Tadeusz', 'Konopielka'],
    1: 123,
    False: 555,
    (1,2): 999
}

print(type(slownik))

# odwolywanie sie do elementow slownika przez operator dostepu
print(slownik['imie'])
print(slownik['nazwisko'])
print(slownik['wiek'])
print(slownik['czy_pelnoletni'])
print(slownik['ulubione_ksiazki'][0])
print(slownik[1])
print(slownik[False])
print(slownik[(1,2)])

# odwlywanie sie do elementow slownik przez metode .get()
print(slownik.get('imie'))
# print(slownik['nr_buta']) # bedzie wyjatek KeyError
print(slownik.get('nr_buta')) # bedzie None
print(slownik.get('nr_buta', 40))

slownik['kolor_wlosow'] = 'blond'
print(slownik)

print('-' * 30)

# standardowa iteracja po slowniku to iteracja po kluczach
for klucz in slownik:
    print(klucz)
    print(slownik[klucz])

print('-' * 30)

print(slownik.keys())
print(slownik.values())

for wartosc in slownik.values():
    print(wartosc)

print('-' * 30)

print(slownik.items())

for klucz, wartosc in slownik.items():
    print(f'{klucz} => {wartosc}')

print('-' * 30)

# taka lista od razu zajmuje ponad 1MB pamięci!!!
duuuuza_lista = [ 303 ] * 1000000

# takie coś wylicza kolejne liczby na żądanie
duzy_zakres = range(1,1000000 )

# takie coś od razu wylicza 999 liczb
duza_lista = [ 10 * x for x in range(1,1000) ]

# takie coś wylicza te liczby dopiero na żądanie
duza_lista2 = ( 10 * x for x in range(1,1000) )
for n in duza_lista2:
    print(n)
    break

print('-' * 30)

xxx = [ 10000000+x for x in range(1,10000) if x % 379 == 0 ]
# w ten sposób od razu wyliczam całą listę wartości
# (a więc zajmuje ona pamięć!!!)
print(xxx)

xxx2 = ( 10000000+x for x in range(1,10000) if x % 379 == 0 )
# powstaje generator, który przechodzi po przekazanej "liście"
# i wylicza wartości dopiero, gdy są one potrzebne
# (a więc oszczędza pamięć)
print(xxx2)
for x in xxx2:
    print(x)

xxx3 = tuple( x**3 for x in range( 1, 8 ) )
print(xxx3)

print('-' * 30)

xxx4 = [ x%5 for x in range(100) ]
print(xxx4)

##############################################

lista = [ "Ala", "Ola", "Ala", "Ula", "Ala", "Ala" ]

# zmieniam na zbiór: --> pozbywam się powtórzeń
print( set(lista) )

# zmieniam z powrotem na listę --> pozbywam się powtórzeń
print( list(set(lista)) )

# wycinam fragment
print( list(set(lista))[1:] )

# odwracam kolejność
print( list(set(lista))[1:][::-1] )

# wyciągam początkowy element
print( list(set(lista))[1:][::-1][0] )

# wyciągam z niego ostatnią literę
print( list(set(lista))[1:][::-1][0][-1] )

# zamieniam ją na wielką literę
print( list(set(lista))[1:][::-1][0][-1].upper() )

##########################################33
print("-----------------------------")

A = { 1, 2, 3, 4, 5, 6 }
B = { 4, 5, 6, 7, 8, 9 }

print(f"A={A}")
print(f"B={B}")

suma_AB = A | B
print(f"suma A i B={suma_AB}")

roznica_AB = A - B
print(f"różnica A i B={roznica_AB}")

iloczyn_AB = A & B
print(f"iloczyn A i B={iloczyn_AB}  (część wspólna)")

rs_AB = A ^ B
print(f"róż. sym A i B={rs_AB}  (elementy będące w dokładnie jednym ze zbiorów)")

# czy dana wartość jest w zbiorze czy nie?

print( 10 in A )
print( 5 in B )

# wyrażenie "listowe" dla zbioru
potegi_2 = { 2**n for n in range(20) }
print(potegi_2)

# wyrażenie "listowe" dla słownika
imiona = ["Mateusz", "Maciej", "Joanna", "Tomasz" ]
imiona2 = {imie : imie[0] + "x" * (len(imie)-1) for imie in imiona}
print(imiona2)

# albo krócej:
imiona3 = {
    imie : imie[0] + "x" * (len(imie)-1)
    for imie in "Mateusz Joanna Maciej Tomasz".split()
}
print(imiona3)
