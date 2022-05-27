import re

kody = [
    '00-123',
    '12323',
    '32-456',
    '43-123',
    '12332'
]

wzorzec = r'[0-9]{2}-?[0-9]{3}'
print(f"Dopasowania do /{wzorzec}/")
r = re.compile(wzorzec)
for kod in kody:
    print(f"{kod}: {r.match(kod)}")

wzorzec = r'([0-9]{2})-?([0-9]{3})'
print(f"Dopasowania do /{wzorzec}/")
r = re.compile(wzorzec)
for kod in kody:
    x = r.match(kod)
    g = x.groups()
    kodn = g[0] + '-' + g[1]
    kodn = f"{g[0]}-{g[1]}"
    print(f"{kod}:  {x}  {g}  POPRAWIONY: {kodn}")

