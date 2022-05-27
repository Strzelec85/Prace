import random

class Osoba:
    def __init__(self, imie, nazwisko, waga, wzrost):
        self._imie = imie
        self._nazwisko = nazwisko
        self._waga = waga
        self._wzrost = wzrost
    def __str__(self):
        return f"{self.imie_i_nazwisko:20s} ({self._waga:5.1f}kg, {self._wzrost:4.2f}m, BMI {self.bmi:4.1f})"
    def __repr__(self):
        return f"{type(self).__name__}{repr((self._imie, self._nazwisko, self._waga, self._wzrost))}"
    def __gt__(self, other):
        return self._waga > other._waga
    def witaj(self, a):
        print(f"Witam {a}! {self}")
    def pokaz_bmi(self):
        print(f"Moje BMI: {self.bmi:.1f}")
    @property
    def bmi(self):
        return self._waga/self._wzrost**2
    @property
    def imie(self):
        return self._imie
    @property
    def imie_i_nazwisko(self):
        return f"{self._imie} {self._nazwisko}"
    def ustaw_imie(self, imie):
        self._imie = imie
    def ustaw_nazwisko(self, nazwisko):
        self._nazwisko = nazwisko
    @staticmethod
    def ocen_zdrowie(bmi):
        # https://pl.wikipedia.org/wiki/Wska%C5%BAnik_masy_cia%C5%82a#Zakresy_warto%C5%9Bci_BMI
        if bmi < 16.0:
            return "wygłodzenie"
        elif bmi < 17.0:
            return "wychudzenie"
        elif bmi < 18.5:
            return "niedowaga"
        elif bmi < 25.0:
            return "ok"
        elif bmi < 30.0:
            return "nadwaga"
        else:
            return "otyłość"
    @classmethod
    def losowa(cls):
        return cls(
            random.choice(["Jan","Maciej","Mateusz","Andrzej","Tomasz",'"Kkkkkk"']),
            random.choice(["A","Bbb","Ccc","Ddd"]),
            random.gauss(70,20),
            random.gauss(1.75, 0.2)
        )

osoby = [Osoba.losowa() for i in range(10)]

osoby.sort()

model = Osoba("XXX", "YYY", 73, 1.91)

for o in osoby:
    if o > model:
        print("OK")
    print(o)


