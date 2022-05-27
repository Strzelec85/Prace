# Najprostsza funkcja przyjmująca od 1 do 4 parametrów

def zlacz( napis1, napis2="", napis3="", napis4="" ):
    return napis1 + napis2 + napis3 + napis4

print(zlacz("Ala"))
print(zlacz("Ala","Ma","Kota"))

def zlacz2( napisy ):
    return "".join( napisy )

# tutaj musimy kolejne napisy przekazać jako listę albo krotkę etc

# to jest krotka (mogłaby też być lista)
imiona = ("Ala","Ma","Kota","A","Ula","Ma","Psa")
print(zlacz2(imiona))
#albo w jednej linii (uwaga na podwójny nawias!)
print(zlacz2(("Ala","Ma","Kota","A","Ula","Ma","Psa")))


# HERE COMES THE MAGIC
def zlacz3( *napisy ):
    return "".join( napisy )
# zlacz3 jest funkcją, która przyjmuje dowolną liczbę parametrów
print(zlacz3("Ala","Ma","Kota","A","Ula","Ma","Psa"))
# argumenty są dostępne w funkcji jako krotka

def zlacz4( lacznik, *napisy ):
    return lacznik.join( napisy )

print(zlacz4("---","Ala","Ma","Kota","A","Ula","Ma","Psa"))

def superfunkcja( *args ):
    print("Wywołano funkcję z parametrami:")
    print(args)
    # tutaj możemy sprawdzać np. ile było argumentów
    if len(args) == 1:
        # zrób coś
        pass
    else:
        # zrób co innego
        pass
    if type(args[0]) == int:
        # zrób coś
        pass
    else:
        # zrób co innego
        pass

superfunkcja( "Józef", 56, 100, True )

def superfunkcja2( **kwargs ):
    print("Wywołano funkcję z parametrami:")
    print(kwargs)
    # w tym momencie można z tym słownikiem zrobić dowolną rzecz

superfunkcja2( imie="Józef", wiek=56 )

def superfunkcja3( *args, **kwargs ):
    print("Wywołano funkcję z parametrami:")
    print(args)
    print(kwargs)

superfunkcja3( 12345, imie="Józef", wiek=56 )
