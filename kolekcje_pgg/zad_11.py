"""
Napisać program, który zamieni numer dnia (0-6) na dwuliterowy symbol dnia tygodnia

0 - Ni
1 - Po
2 - Wt
3 - Śr
4 - Cz
5 - Pi
6 - So

"""
n = int(input("Podaj numer dnia tygodnia (0-6): "))

kod = "NiPoWtŚrCzPiSo"[2*n:2*n+2]
#      ^^               0:2     0
#        ^^             2:4     1
#          ^^           4:6     2
print(f"Kod dnia: {kod}")