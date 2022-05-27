liczby = { int(x) for x in input("Podaj liczby: ").split() } & set(range(0,101,2))

print(f"{liczby}")
