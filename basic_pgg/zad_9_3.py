a = int (input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
operator = input("Podaj operator działanie między liczbami a i b: ")
#     false or true or true or true

# while operator != "+" and operator != "-" and operator != "*" and operator != "/":
while operator not in ("+", "-", "*", "/"):
    operator = input("Podaj poprawny operator działanie między liczbami a i b: ")

if operator == "+":
    wynik = a + b
elif operator == "-":
    wynik = a - b
elif operator == "*":
    wynik = a * b
elif operator == "/":
    wynik = a / b

print(wynik)