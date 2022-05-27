'''
import random

t = []

for x in range(1,11):
    t.append(random.randint(1,100))
    t1 = t[:5]
    t2 = t[-5:]
print(t)
print(t1)
print(t2)

s1 = sum(t1)
s2 = sum(t2)

print(s1)
print(s2)

if t1>t2:
    print("Większa jest t1")
if t1<t2:
    print("Większa jest t2")
if t1==t2:
    print("Są równe")
'''
t = [2.234,432.123]

for  x in t:
    x = round(x,1)

print(t)