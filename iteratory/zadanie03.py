# dopisać generator kazdy_z_kazdym()

def kazdy_z_kazdym(zawodnicy):
    for i in range(len(zawodnicy)):
        grupa = zawodnicy[i+1:]
        zawodnik1 = zawodnicy[i]
        for zawodnik2 in grupa:
            yield zawodnik1, zawodnik2

zawodnicy = ["Mateusz", "Maciej", "Piotr", "Dariusz", "Andrzej"]

for z1, z2 in kazdy_z_kazdym(zawodnicy):
    print(f"* {z1} vs {z2}")
