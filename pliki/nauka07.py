WYS = 32
SZER = 32

f = open("nauka07.pnm", "w")

f.write("P3\n")
f.write(f"{SZER} {WYS}\n")
f.write("255\n")

for y in range(WYS):
    for x in range(SZER):
        f.write("200 0 0\n")
