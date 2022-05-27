# napisać program do przeliczania kursów walut

import requests
import json

# 1. użytkownik podaje kwotę i walutę
# 2. użytkownik podaje drugą walutę

kwota = float(input("Podaj kwotę: "))
waluta = input("Podaj kod waluty: ")
waluta2 = input("Podaj drugą walutę: ")

url1 = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/?format=JSON"
url2 = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta2}/?format=JSON"

kurs1 = json.loads(requests.get(url1).text)['rates'][0]['mid']
kurs2 = json.loads(requests.get(url2).text)['rates'][0]['mid']

print(kwota*kurs1/kurs2)

# 3. program przelicza kwotę z jednej waluty na drugą (wg ostatniego obowiązującego kursu NBP)
