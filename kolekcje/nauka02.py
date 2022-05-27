import collections

oceny = [5,6,5,5,5,4,2,4,5,3,5,4,4,3,4,2,3]

x = collections.Counter(oceny)

for ocena, ilerazy in x.items():
    print(f"{ocena}: {ilerazy}")
