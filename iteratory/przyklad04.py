def dni_tygodnia():
    while True:
        yield "Poniedziałek"
        yield "Wtorek"
        yield "Środa"


for n, d in enumerate(dni_tygodnia()):
    print(d)
    if n == 10: break
