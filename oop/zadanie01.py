class Product:
    def __init__(self, id, nazwa, cena):
        self._id = id
        self._nazwa = nazwa
        self._cena = cena
    def __str__(self):
        return f"Produkt {self._nazwa!r}, id: {self._id} cena: {self._cena:.2f} PLN"
    def print_info(self):
        print(f"{self}")

p1 = Product(1, 'Woda', 10.99)
p1.print_info()
