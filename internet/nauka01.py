# najpierw nalezy w terminalu wykonać polecenie:
# python -m pip install requests
# (alternatywnie:) pip install requests
# jeśli nie mamy wirtualnego środowiska:
# py -m pip install requests

# API NBP: http://api.nbp.pl/

import requests
import json

WALUTA="EUR"

kursy = json.loads(requests.get(f"http://api.nbp.pl/api/exchangerates/rates/A/{WALUTA}/last/30/?format=JSON").text)

for kurs in kursy['rates']:
    print(kurs['mid'])


# inny przykład
# http://wttr.in/Warszawa?format=j1

