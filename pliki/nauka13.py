import os

#katalog bieżący
print("---- KATALOG BIEŻĄCY ----")
for x in os.scandir():
    print(f'{"DIR" if x.is_dir() else "   "}  {x.name}         {x.path}')

#katalog nadrzędny
print("---- KATALOG NADRZĘDNY (..) ----")
for x in os.scandir('..'):
    print(f'{"DIR" if x.is_dir() else "   "}  {x.name}         {x.path}')

#katalog względem bieżącego
print("---- KATALOG basic_pgg (../basic_pgg) ----")
for x in os.scandir('../basic_pgg'):
    print(f'{"DIR" if x.is_dir() else "   "}  {x.name}         {x.path}')

#ścieżka bezwzględna
print("---- KATALOG C:\\Windows ----")
for x in os.scandir('C:/Windows'):
    print(f'{"DIR" if x.is_dir() else "   "}  {x.name}         {x.path}')
