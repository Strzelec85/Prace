# dopisać generator kazdy_z_kazdym()

def kazdy_z_kazdym(zawodnicy):
    for n1, z1 in enumerate(zawodnicy):
        for n2, z2 in enumerate(zawodnicy):
            if n1 < n2:
                yield z1, z2

zawodnicy = ["Mateusz", "Maciej", "Piotr", "Dariusz", "Andrzej"]

for z1, z2 in kazdy_z_kazdym(zawodnicy):
    print(f"* {z1} vs {z2}")
