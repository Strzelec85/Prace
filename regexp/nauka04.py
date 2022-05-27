import re

napis = 'X23 A56 fsdn fh89sdn B39 M34 dkdasjkdasjk M23'

# szukamy symboli składających się z wielkiej litery i 2 cyfr, np. A52
x = re.findall('[ABCDEFGHIJKLMNOPQRSTUVWXYZ][0123456789]{2}', napis)
print(x)

# szukamy symboli składających się z wielkiej litery i 2 cyfr, np. A52
# użycie zakresów w []
x = re.findall('[A-Z][0-9]{2}', napis)
print(x)
