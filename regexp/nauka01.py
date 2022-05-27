# Naiwne podejście do sprawdzania poprawności podanych danych

def poprawny_kod_pocztowy(k):
    if len(k) != 6:
        return False
    if k[2] != '-':
        return False
    if not k[0].isdigit():
        return False
    # i tak dalej
    return True

# 05-510

kod_pocztowy = input("Podaj kod pocztowy: ")

if poprawny_kod_pocztowy(kod_pocztowy):
    print("OK")
else:
    print("Błędny kod")
