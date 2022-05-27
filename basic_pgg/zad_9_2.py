"""
Napisz program, który na podstawie dwóch podanych liczb obliczy wynik zadanej operacji
(dodawanie, odejmowanie, mnożenie, dzielenie). W przypadku podania nieprawidłowej operacji
program ma wyświetlić odpowiedni komunikat o błędzie.

Przykładowy komunikat programu:
Podaj pierwszą liczbę: 10
Podaj drugą liczbę: 5
Podaj rodzaj operacji: +
Wynik: 15
"""

liczba_1 = int(input('Podaj pierwsza liczbe: '))
liczba_2 = int(input('Podaj druga liczbe: '))
operacja = input('Podaj operacje (+, -, *, /): ')

if operacja not in ('+', '-', '*', '/'):
    print("Nieprawidlowy operator!")
    exit()

if operacja == "+":
    wynik = liczba_1 + liczba_2
elif operacja == "-":
    wynik = liczba_1 - liczba_2
elif operacja == "*":
    wynik = liczba_1 * liczba_2
elif operacja == "/":
    wynik = liczba_1 / liczba_2

print(f'Wynik: {wynik}')
