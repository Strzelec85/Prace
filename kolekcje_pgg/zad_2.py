"""
Napisz program obliczający średnią wartość z podanych przez użytkownika liczb.
Do przechowywania liczb użyj listy. Pozwól na wprowadzenie maksymalnie 10 liczb.
Skorzystaj z funkcji wbudowanej sum().
"""

liczby = []
while len(liczby) < 10:
    # x = int(input("Podaj liczbe: "))
    # liczby.append(x)
    liczby.append(int(input("Podaj liczbe: ")))

srednia = sum(liczby) / len(liczby)

print(f"Srednia z wprowadzonych liczb to {srednia:.2f}")
