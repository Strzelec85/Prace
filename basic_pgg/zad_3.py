"""
Napisz program wyliczający kwotę należną za zakupiony
towar na podstawie ceny za kilogram oraz liczby zakupionych kilogramów.
Do przechowywania informacji o cenie oraz liczbie kilogramów użyj zmiennych.
Wypisz wszystkie informacje na konsolę.

Przykładowy komunikat programu:
Cena za kg: 10.0
Waga: 2.5
Należność: 25.0
"""

cena = float(input("Podaj cene: "))
waga = float(input("Podaj wage: "))
naleznosc = cena * waga

print("Cena za kg:", cena, "zł")
print("Waga:", waga, "kg")
print("Należność:", naleznosc, "zł")

print("Cena za kg: " + str(cena) + " zł")
print("Waga: " + str(waga) + " kg")
print("Należność: " + str(naleznosc) + " zł")

print(f"Cena za kg: {cena} zł")
print(f"Waga: {waga} kg")
print(f"Należność: {naleznosc} zł")
