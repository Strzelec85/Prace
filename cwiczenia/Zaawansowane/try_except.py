with open("files.txt", "r") as x:
    pliki = x.read().splitlines()
    print(pliki)
    for i in pliki:
        try:
            plik = open(i)
            print(i + " istnieje")
            plik.close()
        except:
            print(i + " nie istnieje")