class Dlugosc:
    przeliczniki = {
        'm': 1,
        'mm': 0.001,
        'cm': 0.01,
        'dm': 0.1,
        'km': 1000,
        'in': 0.025_4,
        'mi': 1_609.344,
        'ft': 0.304_8
    }
    def __init__(self, wartosc_liczbowa, jednostka):
        self._wartosc_liczbowa = wartosc_liczbowa
        self._jednostka = jednostka
    def __gt__(self, other):
        return self.wartosc_w_m > other.wartosc_w_m
    def __eq__(self, other):
        return self.wartosc_w_m == other.wartosc_w_m
    def __str__(self):
        return f"{self._wartosc_liczbowa:.1f}{self._jednostka}"
    def __repr__(self):
        return f"{type(self).__name__}{repr((self._wartosc_liczbowa, self._jednostka))}"
    def __add__(self, other):
        return type(self)(
            self._wartosc_liczbowa + other.wartosc_w_jednostce(self._jednostka),
            self._jednostka
        )
    def __sub__(self, other):
        # krótsze rozwiązanie:
        # return self + -other
        # tworzy tymczasowy obiekt -other i dodaje go do siebie (potencjalnie mniej wydajne)
        return type(self)(
            self._wartosc_liczbowa - other.wartosc_w_jednostce(self._jednostka),
            self._jednostka
        )
    def __neg__(self):
        return type(self)(
            -self._wartosc_liczbowa,
            self._jednostka
        )
    def __mul__(self, other):
        return type(self)(
            self._wartosc_liczbowa * other,
            self._jednostka
        )
    __rmul__ = __mul__
    # przykład:
    # 7.2 * Dlugosc(3, "m")
    # 7.2 --> other
    # Dlugosc(3, "m") --> self
    # def __rmul__(self, other):
    #    return self * other
    def __truediv__(self, other):
        if type(other) == type(self):
            # tutaj należy zwrócić liczbę oznaczającą stosunek dwóch długości
            return self.wartosc_w_m / other.wartosc_w_m
        else:
            return type(self)(
                self._wartosc_liczbowa / other,
                self._jednostka
            )
    @property
    def wartosc_w_m(self):
        return self._wartosc_liczbowa * self.przeliczniki[self._jednostka]
    def wartosc_w_jednostce(self, jednostka):
        return self.wartosc_w_m / self.przeliczniki[jednostka]
    def przelicz_na(self, jednostka):
        return type(self)(self.wartosc_w_jednostce(jednostka), jednostka)

a = Dlugosc(2, 'km')
b = Dlugosc(3, 'mi')
c = b.przelicz_na('km')
cc = a + c  # zostanie wywołane a.__add__(c)
d = a - b   # zostanie wywołane a.__sub__(b)
e = -c      # zostanie wywołane c.__neg__()
f = a * 3   # zostanie wywołane a.__mul__(3)
g = 4 * b   # zostanie wywołane b.__rmul__(4)
h = b / 6   # zostanie wywołane b.__truediv__(6)
            # dzielenie Dlugosci przez liczbe zwraca inną Długość



dlugosci = [a,b,c,cc,d,e,f,g,h]

for dlugosc in dlugosci:
    print(dlugosc)

a = Dlugosc(2, 'km')
b = Dlugosc(200000, 'cm')
print(a == b)

a = Dlugosc(200, 'km')
b = Dlugosc(126, 'mi')

# to powinno zwrócić liczbę (float)
n = a / b
print(f"Stosunek odległości a do b: {n}")
