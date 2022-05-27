from zipfile import *
plik = input("Podaj nazwę pliku: ")
with ZipFile(plik + ".zip", "r") as z:
   # z.write("files.txt")
   # z.write("n-copy.txt")
   print(z.namelist())
   '''
   for x in z.namelist():
        z.extract(x)

    z.close()
   '''