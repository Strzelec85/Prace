import random

losowa = random.randint(1,100000000000)

napis=f"Losowa liczba: {losowa}"

f = open("nauka02.txt", "w", encoding="UTF-8")
f.write(napis+"\n")
f.write("Fajnie\n")
f.write("Że\n")
f.write("Działa\n")
