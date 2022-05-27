# Napisać program, który zapyta użytkownika o kod waluty
# a następnie pobierze z NBP kurs z ostatnich kilkunastu dni
# i wygeneruje wykres w formacie SVG.

import json
import requests

URL = "http://api.nbp.pl/api/exchangerates/rates/A/%s/last/%d/?format=JSON"

def rysuj_wykres(dane, nazwapliku):
    SZER = 800
    WYS = 600
    MARGIN = 20
    ODSTEP = 10
    f = open(nazwapliku, "w")
    f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
    f.write(f'<svg width="{SZER}" height="{WYS}" xmlns="http://www.w3.org/2000/svg">\n')
    maxwartosc = max([x[1] for x in dane])
    minwartosc = min([x[1] for x in dane])*0.99
    x = MARGIN
    for etykieta, wartosc in dane:
        wysokosc_wzg = (wartosc-minwartosc)/(maxwartosc-minwartosc)
        wysokosc_max = WYS-2*MARGIN
        wysokosc = wysokosc_wzg * wysokosc_max
        szer = (SZER-2*MARGIN-(len(dane)-1)*ODSTEP )/len(dane)
        y = ODSTEP + wysokosc_max - wysokosc
        f.write(f'<rect x="{x:.1f}" y="{y:.1f}" width="{szer:.1f}" height="{wysokosc:.1f}" fill="#f00" stroke="#000" />\n')
        f.write(f'<text x="{x:.1f}" y="{y:.1f}">{wartosc}</text>\n')
        f.write(f'<text x="{x:.1f}" y="{ODSTEP+wysokosc_max:.1f}" transform="rotate(-90, {x},{ODSTEP+wysokosc_max})">{etykieta}</text>\n')
        x+=szer+ODSTEP
    f.write('</svg>')
    f.close()

#waluta = input("Podaj kod waluty: ")
waluta = "EUR"
ile = 12

url = URL % ( waluta, ile )

kursy = [ (k['effectiveDate'], k['mid']) for k in json.loads(requests.get(url).text)['rates'] ]

rysuj_wykres( kursy, "zadanie04.svg")