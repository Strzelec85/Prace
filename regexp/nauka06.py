import re

napisy = [
    "ala ma kota",
    "ala ma psa",
    "ala ma chomika",
    "ala ma koty",
    "ala ma psy"
]

# r'' - surowe stringi (raw strings)

# operator | oznacza albo jeden napis, albo drugi
wzorzec = r'ala ma kota|ala ma psa'
regexp = re.compile(wzorzec)
print(f"WZORZEC: /{wzorzec}/")
for napis in napisy:
    print(f"[{napis}] {'OK' if regexp.match(napis) else '---'}")

# operator | oznacza albo jeden napis, albo drugi
wzorzec = r'ala ma kot[ay]|ala ma psa'
regexp = re.compile(wzorzec)
print(f"WZORZEC: /{wzorzec}/")
for napis in napisy:
    print(f"[{napis}] {'OK' if regexp.match(napis) else '---'}")

# operator | oznacza albo jeden napis, albo drugi
wzorzec = r'ala ma (kot[ay]|ps[ay]|chomika)'
regexp = re.compile(wzorzec)
print(f"WZORZEC: /{wzorzec}/")
for napis in napisy:
    print(f"[{napis}] {'OK' if regexp.match(napis) else '---'}")