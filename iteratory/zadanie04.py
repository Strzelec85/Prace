# Mając listę wartości, policzyć wszystkie możliwe permutacje tej listy.



# np. A B C:
#
# A B C
# A C B
# B A C
# B C A
# C A B
# C B A

def permutacje(elementy):
    #print(f"Permutacje: {elementy}")
    if len(elementy) == 1:
        yield elementy
    # elif len(elementy) == 2:
    #     yield elementy
    #     yield elementy[::-1]
    else:
        for n, e in enumerate(elementy):
            pozostale = elementy[0:n] + elementy[n+1:]
            biezacy = elementy[n:n+1]
            for p in permutacje(pozostale):
                yield biezacy + p

osoby = ('Andrzej', 'Basia', 'Czesław', 'Dariusz', 'Edward', 'Franciszek', 'Grzegorz')

for n, x in enumerate(permutacje(osoby)):
    print(n+1, x)
print("KONIEC")