from .geometria import Dlugosc

# testy pytest
# instalacja pytest: py -m pip install pytest
# instalacja pytest: py -m pip install pytest-html
#
# uruchomienie testów:
#  pytest
# wygenerowanie raportu HTML
#  pytest --html=plik.html

def test_sprawdz_konstruktor_liczba_int_i_jednostka_str():
    d1 = Dlugosc(1, 'm')
    assert type(d1) == Dlugosc

def test__wartosc_z_jednostka_liczba_z_jednostka_str_typ_zwracany():
    assert type(Dlugosc._wartosc_z_jednostka("1m")) == tuple

def test__wartosc_z_jednostka_liczba_z_jednostka_str_dlugosc_krotki():
    assert len(Dlugosc._wartosc_z_jednostka("1m")) == 2

def test__wartosc_z_jednostka_liczba_z_jednostka_str_zawartosc_krotki():
    assert Dlugosc._wartosc_z_jednostka("1m") == (1, "m")

def test__wartosc_z_jednostka_001():
    assert Dlugosc._wartosc_z_jednostka("1km") == (1, "km")

def test__wartosc_z_jednostka_002():
    assert Dlugosc._wartosc_z_jednostka("1mi") == (1, "mi")

def test__wartosc_z_jednostka_003():
    assert Dlugosc._wartosc_z_jednostka("1.5cm") == (1.5, "cm")

def test__wartosc_z_jednostka_004():
    assert Dlugosc._wartosc_z_jednostka("-1.5mm") == (-1.5, "mm")

def test__wartosc_z_jednostka_005():
    assert Dlugosc._wartosc_z_jednostka("-1.5 mm") == (-1.5, "mm")

def test__wartosc_z_jednostka_006():
    assert Dlugosc._wartosc_z_jednostka(" -1.5 mm") == (-1.5, "mm")

def test__konstruktora_001():
    d1 = Dlugosc(1, 'm')
    d2 = Dlugosc('1m')
    assert d1 == d2

def test__konstruktora_002():
    assert Dlugosc('10km') + Dlugosc('20km') == Dlugosc('30km')

def test_porownywanie_001():
    assert Dlugosc('1km') < Dlugosc('1mi')
