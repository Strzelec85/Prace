"""
Napisz program zliczający wystąpienia liczb dodatnich i ujemnych
w zadanej liście liczb całkowitych.
"""

liczby = [1, 2, 3, -100, -10, 0, 4]

ile_dodatnich = 0
ile_ujemnych = 0

for liczba in liczby:
    if liczba > 0:
        ile_dodatnich += 1
    elif liczba < 0:
        ile_ujemnych += 1

print(f'Dodatnich: {ile_dodatnich}, ujemnych: {ile_ujemnych}')
