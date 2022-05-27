class Osoba:
    def __init__(self, imie, nazwisko, waga, wzrost):
        self._imie = imie
        self._nazwisko = nazwisko
        self._waga = waga
        self._wzrost = wzrost
    def witaj(self, a):
        print(f"Witam {a}! {self}")
    def przedstaw_sie(self):
        print(f"Nazywam się {self._imie} {self._nazwisko}")
    def pokaz_bmi(self):
        print(f"Moje BMI: {self.bmi():.1f}")
    def bmi(self):
        return self._waga/self._wzrost**2
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
        elif bmi < 35.0:
            return "otyłość I"
        elif bmi < 40.0:
            return "otyłość II"
        else:
            return "otyłość III"

o1 = Osoba("Jan", "Kowalski", 82, 1.76)
o2 = Osoba("Monika", "Xyz", 50, 1.63)
o3 = Osoba("Basia", "Abc", 123, 1.57)
o4 = Osoba("Wojciech", "Lalala", 78, 1.77)
o5 = Osoba("Grzegorz", "Fff", 73, 1.77)
osoby = [o1, o2, o3, o4, o5, Osoba("Aleksandra", "Ccc", 51, 1.63)]

for o in osoby:
    o.przedstaw_sie()
    ocena = Osoba.ocen_zdrowie(o.bmi())
    print(f"{o.bmi():.1f}: ocena zdrowia: {ocena}")

rozne_bmi = [ 21.3, 19.8, 23.5, 25.7, 27.8, 17.9 ]
for bmi in rozne_bmi:
    print(f"{bmi:.1f}: ocena zdrowia: {Osoba.ocen_zdrowie(bmi)}")