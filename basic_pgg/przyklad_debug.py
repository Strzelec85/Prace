print('Przed petla while')

while True:
    liczba = int(input("Podaj liczbe: "))
    print(f'Twoja liczba to {liczba}')

    if liczba % 2 == 0:
        print("Podales liczbe parzysta, konczymy petle")
        break

print('Jestem poza petla while')