import sqlite3

db = sqlite3.connect("baza1.db")

wynik = db.execute("Select * From osoby;")

for o in wynik:
    print(o)

