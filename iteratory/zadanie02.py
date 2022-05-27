# Napisać generator, który z danego słowa zwróci wszystkie samogłoski

def samogloski(napis):
    SAMOGLOSKI = 'aeuioyAEUIOY'
    for litera in napis:
        if litera in SAMOGLOSKI:
            yield litera

# Przykład:

napis = "Ala ma kota"

for s in samogloski(napis):
    print(f"* {s}")

# ma wyświetlić:
# * A
# * a
# * a
# * o
# * a
