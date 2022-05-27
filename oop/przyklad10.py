def drukuj_swiadectwo(
        imie="##IMIE##",
        nazwisko="##NAZWISKO##",
        klasa="KLASA",
        oceny={"PRZEDMIOT1":0,"PRZEDMIOT2":0}
):
    print(f"-----SWIADECTWO-----")
    print(f"     imie: {imie}")
    print(f" nazwisko: {nazwisko}")
    print(f"UKONCZYL KLASE {klasa}")
    for przedmiot, ocena in oceny.items():
        print(f"{przedmiot}: {ocena}")
    print(f"-----KONIEC-----")


drukuj_swiadectwo(nazwisko="Kowalski", imie="Jan")

# słownik zawierający nazwane argumenty (w dowolnej kolejności)
sw1 = {"klasa":7, "imie":"Janusz", "oceny" : {"matematyka":5,"polski":4}, "nazwisko":"Jjj"}
# użycie go w wywołaniu funkcji:
drukuj_swiadectwo( **sw1 )

# krotka zawierająca kolejne argumenty (w prawidłowej kolejności)
sw2 = ( "Ola","Kowalska",8,{"Polski":6,"Matematyka":6})
# uzycie jej w wywołaniu funkcji:
drukuj_swiadectwo( *sw2 )
