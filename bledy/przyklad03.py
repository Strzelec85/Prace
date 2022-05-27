class PoczatekNiedodatniError(Exception):
    pass

class KoniecMniejszyNizPoczatekError(Exception):
    pass

class WartoscNieparzystaError(Exception):
    def __init__(self, n):
        self._n = n

def czyParzysta(n):
    if n % 2 != 0:
        raise WartoscNieparzystaError(n)

def sprawdzPoczatek(n):
    if n <= 0:
        raise PoczatekNiedodatniError
    czyParzysta(n)

def sprawdzKoniec(n, poczatek):
    if n <= poczatek:
        raise KoniecMniejszyNizPoczatekError
    czyParzysta(n)

try:
    a = int(input("Podaj początek: "))
    sprawdzPoczatek(a)
except ValueError:
    print("Niezrozumiała wartość, ustawiam na 2")
    a = 2
except PoczatekNiedodatniError:
    print("Wartość niedodatnia, ustawiam na 2")
    a = 2
except WartoscNieparzystaError as e:
    print("Wartość nieparzysta, koryguję")
    a = e._n + 1

try:
    b = int(input("Podaj koniec: "))
    sprawdzKoniec(b, a)
except ValueError:
    print("Niezrozumiała wartośc, koryguję")
    b = a + 4
except KoniecMniejszyNizPoczatekError:
    print("Koniec mniejszy niż początek, koryguję")
    b = a + 4
except WartoscNieparzystaError as e:
    print("Wartość nieparzysta, koryguję")
    b = e._n + 1

print("Kolejne liczby:")
for i in range(a,b+1):
    print(i)
print("Koniec")

