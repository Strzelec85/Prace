"""
Napisz program wypisujący na konsolę Twoje imię i wzrost.
Do przechowywania informacji o Twoim imieniu i wzroście użyj zmiennych.

Przykładowy komunikat programu:
Imię: Jan
Wzrost: 180
"""

# imie = 'Piotr'
# wzrost = 180

# input("Pytanie: ") - funkcja do wczytywania danych z konsoli
# funkcja input oddaje, to co uzytkownik wprowadzil
# Uwaga! Funkcja input zawsze zwraca string
imie = input("Podaj imie: ")
# wzrost = input("Podaj wzrost: ")
# wzrost = int(wzrost)

wzrost = int(input("Podaj wzrost: "))

print(type(imie))
print(type(wzrost))

# konkatenację stringów
print('Imie: ' + imie)
print('Wzrost: ' + str(wzrost))

# specyficzny dla funkcji print, bo przekazuje do niej
# wiele argumentow
print('Imie:', imie)
print('Wzrost:', wzrost)

# f-string, formatted-string
print(f'Imie: {imie}')
print(f"Wzrost: {wzrost}")

print('Twoje imie to ' + imie + ' i masz ' + str(wzrost) + 'cm wzrostu.')
print(f'Twoje imie to {imie} i masz {wzrost}cm wzrostu.')
