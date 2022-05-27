# wygenerować obrazek PNM o rozmiarze 32x32
# zawierający naprzemiennie dwa kolory (dowolne)

SZER = 32
WYS = 32

f = open("zadanie02.pnm", "w")
f.write(f"P3 {SZER} {WYS} 255\n")

for y in range(WYS):
    for x in range(SZER):
        if y % 2 == 0:
            f.write("255 128 0\n")
        else:
            f.write("10 250 10\n")
