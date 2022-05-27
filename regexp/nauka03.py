import re
napis = "kat kot kaot koooooot kooooooooooooooooooot koooaaaoaoaoaot kt pies"

# plus oznacza powtórzenie ostatniego elementu dowolną liczbę razy >= 1
x = re.findall('k[oa]+t', napis)
print(x)

# tutaj plus dotyczy literki "o"
x = re.findall('ko+t', napis)
print(x)

# gwiazdka oznacza powtórzenie ostatniego elementu dowolną liczbę razy >= 0
x = re.findall('k[oa]*t', napis)
print(x)

# znak zapytania oznacza że ostatni element albo jest albo go nie ma (0 lub 1 raz)
x = re.findall('k[oa]?t', napis)
print(x)

# nawiasy klamrowe oznaczają wystąpienie wskazaną liczbę razy (tutaj 6)
x = re.findall('k[oa]{6}t', napis)
print(x)

# nawiasy klamrowe oznaczają wystąpienie od 2 do 10 razy włącznie
x = re.findall('k[oa]{2,10}t', napis)
print(x)

# nawiasy klamrowe oznaczają wystąpienie co najmniej 4 razy
x = re.findall('k[oa]{4,}t', napis)
print(x)

# nawiasy klamrowe oznaczają wystąpienie co najwyżej 10 razy
x = re.findall('k[oa]{,10}t', napis)
print(x)



