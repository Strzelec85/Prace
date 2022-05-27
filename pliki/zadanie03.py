# wczytać uczniów z pliku `uczniowie.json`
# policzyć średnią
# do pliku `najlepsi.json` wpisać 3 uczniów z najwyższą średnią w formacie:
# [
#   {
#    "kto" : "Jan K.",
#    "srednia" : 4.45
#   },
# ...
# ]

import json

def srednia(oceny):
    return sum(oceny)/len(oceny)

uczniowie = json.load(open("uczniowie.json", encoding="UTF-8"))

uczniowie.sort(key=lambda u:srednia(u['oceny']))

najlepsi = [ { "kto" : f"{u['imie']} {u['nazwisko']}", "srednia" : srednia(u['oceny']) } for u in uczniowie[-3:]]

json.dump(najlepsi, open("najlepsi.json", "w", encoding="UTF8"), indent=2)

