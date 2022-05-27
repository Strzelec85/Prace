# uwaga: plik przyklad01.txt nie może istnieć!!!

try:
    tekst = open("przyklad01.txt").read()
except:
    print("Coś się zepsuło.")
    tekst = "***"

print(f"Tekst z pliku: {tekst}")


