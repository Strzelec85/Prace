"""
Korzystając z przypisywania wartości do zmiennych,
napisz program obliczający pole trapezu
o długości podstaw 3 i 9 oraz wysokości 6.5.
"""

podstawa_1 = 3
podstawa_2 = 9
wysokosc = 6.5
pole_trapezu = 1 / 2 * (podstawa_1 + podstawa_2) * wysokosc

print(pole_trapezu)
print("Pole trapezu wynosi: " + str(pole_trapezu))

# jak przekazuje wiele argumentow do print
# to print automatycznie oddziela je od siebie spacja
print(podstawa_1, podstawa_2, wysokosc, pole_trapezu)

print("Pole trapezu wynosi:", pole_trapezu)
