"""
Napisz program obliczający koszt przejazdu z miasta A do B na podstawie podanej
przez użytkownika liczby kilometrów, ceny paliwa oraz spalania.
Zapytaj użytkownika także o nazwy miejscowości.

Przykładowe komunikaty programu:
Miasto A: Warszawa
Miasto B: Gdańsk
Dystans Warszawa-Gdańsk: 420
Cena paliwa: 4.55
Spalanie na 100 km: 5.5
Koszt przejazdu Warszawa-Gdańsk to 105 PLN

100 km - spalanie
dystans - x
"""

miasto_a = input("Podaj miasto A: ")
miasto_b = input("Podaj miasto B: ")
dystans = int(input(f"Podaj dystans na trasie {miasto_a}-{miasto_b}: "))
cena_paliwa = float(input("Cena paliwa: "))
spalanie = float(input("Spalanie na 100 km: "))

koszt = dystans / 100 * spalanie * cena_paliwa

print(f'Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:.2f} PLN')
