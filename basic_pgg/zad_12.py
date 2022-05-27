"""
Napisz program wyświetlający minimalną oraz maksymalną liczbę z wszystkich
liczb wprowadzonych liczb przez użytkownika.

Daj użytkownikowi możliwość zakończenia wprowadzania liczb odpowiednią komendą (np. KONIEC).
Zadbaj o obsłużenie przypadku gdy użytkownik nie wprowadzi żadnej liczby.
"""

znalezione_minimum = None
znalezione_maksimum = None

while True:
    # funkcja input ZAWSZE zwraca string!
    dane_wejsciowe = input("Podaj liczbe lub wpisz KONIEC: ")
    if dane_wejsciowe.upper() == "KONIEC":
        break

    liczba = int(dane_wejsciowe)
    if znalezione_minimum is None or liczba < znalezione_minimum:
        znalezione_minimum = liczba

    if znalezione_maksimum is None or liczba > znalezione_maksimum:
        znalezione_maksimum = liczba

if znalezione_minimum is not None and znalezione_maksimum is not None:
    print(f'Znalezione minimum: {znalezione_minimum}')
    print(f'Znalezione maksimum: {znalezione_maksimum}')
else:
    print('Nie podales liczb!')
