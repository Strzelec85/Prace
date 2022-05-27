import sqlite3

db = sqlite3.connect("baza1.db")

wynik = db.execute("""
    Select imie, count(*)
    From osoby
    Group By imie
""")

for o in wynik:
    print(o)

