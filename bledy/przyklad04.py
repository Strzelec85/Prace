import json

try:
    dane = json.load(open("przyklad04.json", encoding="UTF8"))
except FileNotFoundError as e:
    print(f"Plik nie istnieje: {e.filename}")
    dane = None
except json.decoder.JSONDecodeError as e:
    print(f"Niepoprawny JSON:")
    print(f"Komunikat: {e.msg}")
    print(f"------------\n{e.doc}\n-------------")
    print(f"Linia: {e.lineno}")
# |  msg: The unformatted error message
# |  doc: The JSON document being parsed
# |  pos: The start index of doc where parsing failed
# |  lineno: The line corresponding to pos
# |  colno: The column corresponding to pos
    dane = None

print(dane)
