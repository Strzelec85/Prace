import datetime
import json

class NiktTyleNieZyje(Exception):
    pass

class PoborowySieNieNadaje(Exception):
    pass

class PoborowyZaStary(PoborowySieNieNadaje):
    def __init__(self, wiek):
        self.wiek = wiek

class PoborowyNiezdrowy(PoborowySieNieNadaje):
    def __init__(self, bmi):
        self.bmi = bmi

class PoborowyZaNiski(PoborowySieNieNadaje):
    def __init__(self, wzrost):
        self.wzrost = wzrost

class Osoba:
    def __init__(self, imie, nazwisko, waga, wzrost, rok_urodzenia):
        self._imie = imie
        self._nazwisko = nazwisko
        try:
            assert type(nazwisko) == str
        except:
            raise TypeError
        self._waga = waga
        self._wzrost = wzrost
        self._rokur = rok_urodzenia
        try:
            assert self.wiek <= 150
        except:
            raise NiktTyleNieZyje
    @property
    def bmi(self):
        return self._waga/self._wzrost**2
    def __repr__(self):
        return f"{type(self).__name__}{repr((self._imie, self._nazwisko, self._waga, self._wzrost, self._rokur))}"
    @property
    def wiek(self):
        return datetime.date.today().year - self._rokur

class Poborowy(Osoba):
    def __init__(self, imie, nazwisko, waga, wzrost, rok_urodzenia, rok_poboru):
        super().__init__(imie, nazwisko, waga, wzrost, rok_urodzenia)
        self._rokpob = rok_poboru

    def __repr__(self):
        return f"{type(self).__name__}{repr((self._imie, self._nazwisko, self._waga, self._wzrost, self._rokur, self._rokpob))}"

    @classmethod
    def rekrutuj(cls, osoba):
        cls.sprawdz_osobe(osoba)
        return cls(
            osoba._imie,
            osoba._nazwisko,
            osoba._waga,
            osoba._wzrost,
            osoba._rokur,
            datetime.date.today().year
        )

    @staticmethod
    def sprawdz_osobe(osoba):
        try:
            assert osoba.wiek < 30
        except:
            raise PoborowyZaStary(osoba.wiek)

        try:
            assert 19 < osoba.bmi < 28
        except:
            raise PoborowyNiezdrowy(osoba.bmi)

        try:
            assert osoba._wzrost > 1.45
        except:
            raise PoborowyZaNiski(osoba._wzrost)


osoby = json.load(open("przyklad05.json", encoding="UTF-8"))

poborowi = []

for o in osoby:
    try:
        osoba = Osoba(**o)
    except TypeError:
        print(f"Nie udało się przekształcić osoby: {o}")
        continue
    except NiktTyleNieZyje:
        print(f"Jakiś długowieczny: {o}")
        continue
    print(f"* {osoba}")
    try:
        poborowy = Poborowy.rekrutuj(osoba)
    except PoborowySieNieNadaje as e:
        print("Nie nadaje się")
        continue
    # except PoborowyZaStary as e:
    #     print(f"Za stary (wiek: {e.wiek}): {osoba}")
    #     continue
    # except PoborowyNiezdrowy as e:
    #     print(f"Za stary (bmi: {e.bmi}): {osoba}")
    #     continue
    # except PoborowyZaNiski as e:
    #     print(f"Za niski: {osoba}")
    #     continue
    poborowi.append(poborowy)

print("--------------")
for p in poborowi:
    print(p)

