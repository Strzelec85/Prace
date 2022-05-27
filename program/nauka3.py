import nauka.geometria
from nauka import geometria
from nauka.geometria import Dlugosc

d1 = nauka.geometria.Dlugosc(6, 'km')
d2 = nauka.geometria.Dlugosc(4, 'mi')
print(d1 + d2)

d3 = geometria.Dlugosc(1, 'km')
d4 = geometria.Dlugosc(1, 'mi')
print(d3 + d4)

print(Dlugosc(5,'m') + Dlugosc(14,'ft'))
