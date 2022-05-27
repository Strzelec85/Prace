import json

f = open("osoby.json", "r", encoding="UTF-8" )

osoby = json.load( f )

for osoba in osoby:
    print(f"{osoba['imie']} {osoba['nazwisko']}")

firma = {
    "nazwa" : "ABCD Company",
    "gieldowa" : True,
    "ostatnie notowania" : [5.06, 5.07, 5.10, 5.09 ]
}

tekst = json.dumps(firma)
print(tekst)

f = open("firma.json","w",encoding="UTF-8")
json.dump(firma, f, indent=4)
