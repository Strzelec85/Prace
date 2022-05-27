def rowne_kroki(poczatek, koniec, ile):
    print("Generuje listę kroków")
    krok = (koniec - poczatek)/(ile - 1)
    for i in range(ile):
        print("Dodaję krok")
        yield poczatek + i*krok
    print("Koniec generowania")

print("Rozpoczynam pętlę:")
for i in rowne_kroki(200,3000000,1700000):
    print(f"glowna petla: {i}")
    if i > 100000:
        break

