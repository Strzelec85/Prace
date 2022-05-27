"""
Napisz program, który sprawdzi pełnoletność osoby na podstawie roku jej urodzenia.

Przykładowy komunikat programu:
Podaj rok urodzenia: 1980
Jesteś pełnoletni!
"""

rok_urodzenia = int(input('Podaj rok urodzenia: '))
wiek = 2020 - rok_urodzenia

if wiek >= 18:
    print('Jestes pelnoletni')
else:
    print('NIE jestes pelnoletni')

