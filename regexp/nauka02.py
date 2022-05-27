import re

napis = 'ala ma kota a ula ma psa a ola ma chomika aga iza'

x = re.findall('[auoi][lgz]a', napis)
print(x)
