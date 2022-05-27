poczatek = 100
koniec = 115
ile_elem = 17

krok = (koniec - poczatek)/(ile_elem - 1)

print(f"krok={krok}")
for i in range(ile_elem):
    print(f"* {poczatek + i*krok}")
