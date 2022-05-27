import sys
import random

print("Dzien dobry")
print("Jestem programem")
print("Koniec")

print(sys.argv)

if len(sys.argv) > 1:
    nazwapliku = sys.argv[1]
    print(f"Zapiszę do pliku: {nazwapliku}")

    with open(nazwapliku,"w") as f:
        f.writelines([str(random.randint(0,100))+"\n" for x in range(10)])
else:
    print("Podaj nazwę pliku")