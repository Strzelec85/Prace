import os

sciezka_wzg = "../oop/../../../../../Windows/System32"
sciezka_abs = os.path.abspath(sciezka_wzg)
sciezka_zak = r'C:\Windows'
x = os.path.commonpath((sciezka_abs, sciezka_zak))
print(x == sciezka_zak)

