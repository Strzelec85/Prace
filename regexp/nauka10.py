import re

napis = """Tralalala m.adamowski@alx.pl hihihi biuro@alx.pl
cokolwiek innego admin@gmail.com kontakt@firma.com.pl
i jakieś inne adresy:
* wojtek81@costam.pl
* blabla123@hihi-hihi.net
abc@xyz
No i to tyle
"""

# Zamień pasujące wzorce na inny napis
wzorzec = re.compile(r'[-\w.]+@[-\w.]+')
napis2 = re.sub(wzorzec, 'XXXXX', napis)
print(napis2)
print("--------------")
wzorzec = re.compile(r'([-\w.]+@[-\w.]+)')
napis2 = re.sub(wzorzec, r'(((\1)))', napis)
print(napis2)
print("--------------")
wzorzec = re.compile(r'([-\w.]+)@([-\w.]+)')
napis2 = re.sub(wzorzec, r'\1@xxx', napis)
print(napis2)
print("--------------")
wzorzec = re.compile(r'([-\w.]+)@([-\w.]+)')
# .sub() może być metodą modułu re
# lub skompilowanego wzorca
# ale różni się wtedy listą argumentów
napis2 = wzorzec.sub(r'xxx@\2', napis)
print(napis2)
