import collections

napis = "Ala ma kota a kot ma psa a pies ma budę"

x = collections.Counter(napis)

for litera, ilerazy in x.items():
    print(f"{litera}: {ilerazy}")
