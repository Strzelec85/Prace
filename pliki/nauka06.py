f = open("uczniowie.txt", "r", encoding="UTF-8")

for linia in f:
    linia = linia.strip()
    kolumny = linia.split(",")
    print(f"Linia: {kolumny}")
