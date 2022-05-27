"""
Wygenerować zbiór krotek zawierajacych 3 elementy:
 - dana liczbe
 - jej kwadrat i
 - jej szescian
Dla liczb w przedziale od -10 do 10
"""

z = { (x, x**2, x**3) for x in range(-10,11) }

print(z)