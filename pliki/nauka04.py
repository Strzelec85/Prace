f = open("nauka03.txt", "rb")

# wczytaj 3 bajty
print(f.read(3))

# przesuń o jeden bajt do przodu
f.seek(1, 1)

# wczytaj 2 bajty
print(f.read(2))
