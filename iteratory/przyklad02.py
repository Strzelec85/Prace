def rowne_kroki(poczatek, koniec, ile):
    print("Generuje listę kroków")
    krok = (koniec - poczatek)/(ile - 1)
    wynik = []
    for i in range(ile):
        print("Dodaję krok")
        wynik.append(poczatek + i*krok)
    print("Koniec generowania")
    return wynik

print("Rozpoczynam pętlę:")
for i in rowne_kroki(200,3000000,17):
    print(i)

