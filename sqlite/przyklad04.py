import sqlite3

db = sqlite3.connect("baza1.db")

wynik = db.cursor().execute("""
    Insert Into osoby
    Values ('Konstanty', 'Iksinski', 70, 1.80, 1970)
""", ())

db.commit()

#print(wynik)

