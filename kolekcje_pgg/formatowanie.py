imie = "Mateusz"
firma = "ALX"
punkty = 98
wzrost = 1.79

print(f"Imie: [{imie}]  firma: [{firma}]  punkty: [{punkty:10d}] wzrost: [{wzrost:.4f}]")

print("Imie: [%s]" % imie )
print("Imie: [%s] firma: [%s]" % ( imie, firma ) )
print("Imie: [%s] firma: [%s]  punkty: [%10d]  wzrost: [%.3f]" % ( imie, firma, punkty, wzrost ) )


print("Imie [{0:10s}] Firma {1}".format( "Mateusz", "ALX" ) )

