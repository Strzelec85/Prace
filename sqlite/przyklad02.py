import sqlite3

db = sqlite3.connect("baza1.db")

wynik = db.execute("""
    Select imie, nazwisko, wzrost
    From osoby
    Where wzrost > 1.60
    Order by nazwisko, imie
""")

for o in wynik:
    print(o)

