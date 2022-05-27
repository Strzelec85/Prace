# wygenerowac obrazek PNM z płynnym przejściem jednego koloru w inny
# użyć generatorów

def przejscie(kolor1, kolor2, kroki):
    r1, g1, b1 = kolor1
    r2, g2, b2 = kolor2
    dr = (r2-r1)/(kroki-1)
    dg = (g2-g1)/(kroki-1)
    db = (b2-b1)/(kroki-1)
    for i in range(kroki):
        yield (int(r1), int(g1), int(b1))
        r1 += dr
        g1 += dg
        b1 += db

kolor1 = (239, 0, 64)
kolor2 = (255, 255, 0)

# 239   0  32
# 243  64  24
# 247 128  16
# 251 192   8
# 255 255   0

for kolor in przejscie(kolor1, kolor2, 5):
    print(kolor)

SZER, WYS = 64, 64

with open("zadanie01.pnm", "w") as f:
    f.write(f"P3 {SZER} {WYS} 255\n")
    for y in range(WYS):
        for r, g, b in przejscie(kolor1, kolor2, SZER):
            f.write(f"{r} {g} {b}\n")
