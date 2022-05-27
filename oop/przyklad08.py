class Robot:
    def __init__(self, model, numer_seryjny):
        self._model = model
        self._numer_seryjny = numer_seryjny
    def __repr__(self):
        return f"{self.__class__.__name__}{repr((self._model, self._numer_seryjny))}"
    def pracuj(self, czas):
        print(f"{self._numer_seryjny}: PR-A-C-U-JĘ {czas}h")

class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko=None):
        self._imie = imie
        self._nazwisko = nazwisko
        self._stanowisko = stanowisko
        self._stawka = 0
        self._zarobione = 0.0
    def ustaw_stawke(self, stawka):
        self._stawka = stawka
    def pracuj(self, czas):
        print(f"{self._imie}: Pracuję {czas}h")
        self._zarobione += self._stawka * czas
    def raport(self):
        print(f"{self._imie:10} {self._nazwisko:10} ({self._stanowisko}): {self._stawka:.2f}/h  {self._zarobione:.2f}")
    def __repr__(self):
        return f"{self.__class__.__name__}{repr((self._imie, self._nazwisko, self._stanowisko))}"

class Menedzer(Pracownik):
    def __init__(self, imie, nazwisko, stanowisko=None, pracownicy=[]):
        # najpierw wołam konstruktor klasy nadrzędnej
        super().__init__(imie, nazwisko, stanowisko)
        # potem dokonuję inicjacji własnych atrybutów
        self._pracownicy = pracownicy
    def dodaj_pracownika(self, pracownik):
        self._pracownicy.append(pracownik)
    def raport_pracownikow(self):
        for p in self._pracownicy:
            p.raport()
    def raport(self):
        super().raport()
        print(f"{self._imie:10} {self._nazwisko:10} ({self._stanowisko}): Liczba podwładnych: {len(self._pracownicy)}")
    def pracuj(self, czas):
        print(f"{self._imie}: Menedżeruję {czas}h")
        self._zarobione += self._stawka * czas

class Prezes(Menedzer):
    pass

print("----- Tworzenie pracowników")

p1 = Pracownik("Jan", "Kowalski")
p2 = Pracownik("Janusz", "Kowalczyk")

p3dane = { "imie" : "Barbara", "nazwisko" : "Kowalska", "stanowisko" : "sekretarka" }
p3 = Pracownik(**p3dane)

m1 = Menedzer("Andrzej", "Z", pracownicy=[p1, p2, p3] )


print("----- Zmuszanie ich do pracy")
p1.ustaw_stawke(47.50)
p1.pracuj(7.0)
p2.ustaw_stawke(43.50)
p2.pracuj(8.0)
m1.ustaw_stawke(300)
m1.pracuj(1.0)
#m1.dodaj_pracownika(p1)
#m1.dodaj_pracownika(p2)
m1.raport_pracownikow()
m1.raport()

r1 = Robot("ZXX400","a789ss78a")
zasoby = [p1,p2,r1,m1]

print("----- Zmuszanie ich do pracy")

for z in zasoby:
    z.pracuj(1)

print("----- Wzywanie ich do raportu")

pracownicy = [p1,p2,m1]
for p in pracownicy:
    p.raport()


# m1.ustaw_stawke(300)
# m1.pracuj(4.0)
# m1.raport()

# print(p1)
# print(m1)

#p2 = Pracownik("Henryk", "Kowalczyk", "hydraulik")
#m1 = Menedzer("Andrzej", "Z")
#print(p1)

#pracownicy = [p1,p2,m1]

#print(pracownicy)
