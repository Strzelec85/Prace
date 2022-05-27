import re

napis = "cokolwiek 102.13.45.12 coś 123...5678 innego 45.56.123.30 67.3.8.90 oraz 30.45.131.123 123.260.34.45"

wzorzec = r'[0-9]+\.'
print(f"/{wzorzec}/: {re.findall(wzorzec, napis)}")

wzorzec = r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
print(f"/{wzorzec}/: {re.findall(wzorzec, napis)}")

wzorzec = r'[0-9]+\.{3}[0-9]+'
print(f"/{wzorzec}/: {re.findall(wzorzec, napis)}")

# notacja ?:
# powoduje, że nawiasy mają TYLKO znaczenie grupujące (grouping)
# a nie łapiące (capturing)
wzorzec = r'(?:[0-9]+\.){3}[0-9]+'
print(f"/{wzorzec}/: {re.findall(wzorzec, napis)}")

# \d - cyfra (digit)
wzorzec = r'(?:\d+\.){3}\d+'
print(f"/{wzorzec}/: {re.findall(wzorzec, napis)}")

# niby tak, ale jednak nie :-)
wzorzec = r'(?:\d+\.?){4}'
print(f"/{wzorzec}/: {re.findall(wzorzec, napis)}")