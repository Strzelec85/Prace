import re

napis = "tralala.com e.commerce.net qwe.cam abc.c0m xyz.c+m www.google2.com minicom dotcom slashdot.net cokolwiek.com.pl firma.com.pl"

# kropka oznacza DOWOLNY znak
wzorzec = r'[a-z]+.c.m'
x = re.findall(wzorzec, napis)
print(f"WZORZEC: /{wzorzec}/  DOPASOWANIA: {x}")

# kropka oznacza DOWOLNY znak
wzorzec = r'[a-z]+.com'
x = re.findall(wzorzec, napis)
print(f"WZORZEC: /{wzorzec}/  DOPASOWANIA: {x}")

# kropka oznacza DOWOLNY znak
wzorzec = r'[a-z]+\.com'
x = re.findall(wzorzec, napis)
print(f"WZORZEC: /{wzorzec}/  DOPASOWANIA: {x}")

# \b oznacza granicę (boundary) słowa
wzorzec = r'[a-z]+\.com\b'
x = re.findall(wzorzec, napis)
print(f"WZORZEC: /{wzorzec}/  DOPASOWANIA: {x}")

# \w oznacza fragment słowa (word) - gdzie słowo składa się z liter i cyfr
wzorzec = r'\w+\.com\b'
x = re.findall(wzorzec, napis)
print(f"WZORZEC: /{wzorzec}/  DOPASOWANIA: {x}")
