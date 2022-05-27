# wygenerowac obrazek PNM z płynnym przejściem jednego koloru w inny
# użyć generatorów

def rowne_kroki(poczatek, koniec, ile):
    krok = (koniec - poczatek)/(ile - 1)
    for i in range(ile):
        yield poczatek + i*krok

def przejscie(kolor1, kolor2, kroki):
    r1, g1, b1 = kolor1
    r2, g2, b2 = kolor2
    for r, g, b in zip(
            rowne_kroki(r1, r2, kroki),
            rowne_kroki(g1, g2, kroki),
            rowne_kroki(b1, b2, kroki),
    ):
        yield r, g, b

kolor1 = (96, 0, 128)
kolor2 = (255, 128, 0)

# 239   0  32
# 243  64  24
# 247 128  16
# 251 192   8
# 255 255   0

for kolor in przejscie(kolor1, kolor2, 5):
    print(kolor)

SZER, WYS = 64, 64

with open("zadanie01bis.pnm", "w") as f:
    f.write(f"P3 {SZER} {WYS} 255\n")
    for y in range(WYS):
        for r, g, b in przejscie(kolor1, kolor2, SZER):
            f.write(f"{r} {g} {b}\n")
