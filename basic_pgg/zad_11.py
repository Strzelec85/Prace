"""
Napisz program obliczający średnią wartość temperatury w danym tygodniu
na podstawie temperatur wprowadzonych przez użytkownika.
"""

numer_dnia = 1
suma_temperatur = 0
LICZBA_DNI = 7

while numer_dnia <= LICZBA_DNI:
    suma_temperatur += int(input(f"Podaj temperature z dnia {numer_dnia}: "))
    numer_dnia += 1

# LICZBA_DNI = 1

srednia_temperatur = suma_temperatur / LICZBA_DNI

print(f'Srednia temperatura w tygodniu to {srednia_temperatur:.1f}')
