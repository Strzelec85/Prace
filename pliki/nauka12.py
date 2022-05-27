import re
import os

wzorzec = re.compile(r'nauka[0-9]+\.txt')

for nazwa in os.listdir():
    if not wzorzec.match(nazwa):
        continue
    print(f"-- {nazwa} --")
    with open(nazwa,"r", encoding="utf-8") as f:
        print(f.read())
    print("---------------")

print([nazwa for nazwa in os.listdir() if wzorzec.match(nazwa)])
