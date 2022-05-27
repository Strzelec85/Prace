
try:
    with open("C://Windowsw/abc.txt", "w") as abc:
        abc.write("test")
except FileNotFoundError:
    # tu moglibyśmy np. utworzyć taki katalog...
    print("Błąd: katalog nie istnieje")
except PermissionError:
    print("Brak dostępu")
