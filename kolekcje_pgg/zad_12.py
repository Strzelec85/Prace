"""
Napisz program zliczajacy liczbe unikalnych liczb wprowadzonych
przez uzytkownika. Sprawdz jak duzo z tych liczb jest liczbami
parzystymi w zakresie 0-100.
"""

liczby = set()

while True:
    x = input("Podaj liczbe (lub KONIEC):")
    if x.lower() == 'koniec':
        break
    xx = int(x)
    liczby.add(xx)

liczby = liczby & set(range(0,101,2))

print(f"Zbiór: {liczby}")
print(f"Liczba elementów: {len(liczby)}")

