# Zaimplementuj klase Employee umozliwiajaca rejestrowanie czasu
# pracy oraz wypłacanie pensji na podstawie zadanej stawki
# godzinowej. Jezeli pracownik bedzie pracował wiecej niz 8 godzin
# (podczas pojedynczej rejestracji czasu) to kolejne godziny policz
# jako nadgodziny (z podwójna stawka godzinowa).
# Przykład uzycia:
# >>> employee = Employee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> employee.pay_salary()
# 500.0
# >>> employee.pay_salary()
# 0.0
# >>> employee.register_time(10)
# >>> employee.pay_salary()
# 1200.0

class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self._imie = imie
        self._nazwisko = nazwisko
        self._stawka = stawka
        self._zarobione = 0
    def register_time(self, czas):
        self._zarobione += self._stawka * ( czas if czas <= 8 else ( 8 + 2 * ( czas - 8 ) ) )
    def pay_salary(self):
        x = self._zarobione
        self._zarobione = 0
        return x

e1 = Employee("Jan","Kowalski",100.0)
e1.register_time(7)
print( e1.pay_salary() )
