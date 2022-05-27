"""
Mam listę liczb w zmiennej a.
chcemy w zmiennej b stworzyć listę zawierającą jedynie liczby większe od 50
b ma mieć zawartość: [400, 90, 100, 234 ... ] itd
"""

a = [1, 400, 3, 7, 20, 90, 100, 234, 3423, 40, 4343, 1, 1000 ]
b = []

for x in a:
    if x > 50:
        b.append( x )

print(b)