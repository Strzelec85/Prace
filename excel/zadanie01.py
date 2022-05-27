# instalacja modułu openpyxl:
# py -m pip install openpyxl
# dokumentacja:
# https://openpyxl.readthedocs.io/en/stable/usage.html

# wczytać informacje o tankowaniach z pliku json
# i wygenerować raport w formacie Excela

import openpyxl
import json

tankowania = json.load(open("zadanie01.json"), encoding="UTF-8")

wb = openpyxl.Workbook()
ws = wb.active
ws.append(list(tankowania[0].keys()) + ["koszt"] )
for tankowanie in tankowania:
    ws.append(
        list(tankowanie.values()) + ["=C:C*D:D"]
    )

wb.save("zadanie01.xlsx")