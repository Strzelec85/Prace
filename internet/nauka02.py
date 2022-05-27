import random

def formatPL(n):
    return str(n).replace(".",",")

f = open("nauka02.csv", "w")

for i in range(20):
    a = random.randint(1, 100)
    b = random.uniform(0, 400)
    c = random.gauss(100, 10)
    f.write(f"{formatPL(a)};{formatPL(b)};{formatPL(c)}\n")

