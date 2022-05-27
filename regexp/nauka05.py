import re

kody = ['01-456', '23-b34', '00-000', '12345', '34-554', 'brak', 'xx-xxx', 'abc00-123x', ' 00-123', '00-456 Warszawa']

wzorzec = re.compile('[0-9]{2}-[0-9]{3}$')

for kod in kody:
    x = wzorzec.match(kod)
    print(kod, "OK" if x else "BLAD", x.group() if x is not None else "---")

