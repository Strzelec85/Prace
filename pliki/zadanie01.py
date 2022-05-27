# wczytać dane z pliku tankowania.txt
# dla każdego tankowania podać koszt paliwa
# podać sumaryczny koszt paliwa

kosztCalk = 0.0
for linia in open("tankowania.txt"):
    kolumny = linia.strip().split(',')
    obj = float(kolumny[2])
    cena = float(kolumny[3])
    koszt = obj * cena
    kosztCalk += koszt
    print(f"Tankowanie {obj}L * {cena} PLN = {koszt:.2f} PLN")

print(f"Razem: {kosztCalk:.2f} PLN")

# Zakładając, że każde tankowanie było do pełna, policzyć spalanie na każdym odcinku.
# Policzyć:
# - koszt dzienny na każdym tankowaniu
# - średni koszt dzienny w całym okresie
# - średni koszt miesięczny na całym okresie
# - średni przebieg dzienny
# - średnie zużycie paliwa na 100km (na każdym tankowaniu osobno i sumarycznie)
# - itd
