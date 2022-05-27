from datetime import datetime
from datetime import timedelta

d = datetime.now()
# formatowanie domyślne
print(d)

# formatowanie funkcją strftime
print(d.strftime("%Y/%m/%d %H:%M"))

# konkretne składowe
print(d.year + 1)

# konkretna data zamiast teraźniejszej
d2 = datetime(1900,12,24)
print(d2)

# inna data
d3 = datetime(1997, 1, 31)
print(d3)

# to zadziała, bo daty można odejmować i wychodzi interwał (timedelta)
x = d3 - d2
print(x)

# to nie zadziała, bo nie da się dodawać dat
try:
    x2 = d3 + d2
except:
    print("Nie działa, bo nie da się dodawać dat")

x3 = timedelta(40)
print(d2 + x3)

x4 = timedelta(hours=1000)
print(d2 + x4)


# d7 = datetime.strptime("next monday")
# print(d7)
