from nauka.geometria import Dlugosc

d1 = Dlugosc(1, 'm')
assert type(d1) == Dlugosc



x = Dlugosc._wartosc_z_jednostka("1m")
assert type(x) == tuple
assert len(x) == 2
assert x == (1, "m")

d1 = Dlugosc(1, 'm')
d2 = Dlugosc('1m')
assert d1 == d2



