import random

f = open("nauka10.svg", "w", encoding="UTF-8")

f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
f.write('<svg width="800" height="800" xmlns="http://www.w3.org/2000/svg">')
f.write('<style>.podpis { font-family: "Tahoma", sans-serif; font-size: 20px; }</style>')

for i in range(15):
    x = random.randint(0, 600)
    y = random.randint(0, 600)
    wys = random.randint(100, 200)
    szer = random.randint(100, 200)
    f.write(f'<rect fill="#f00" stroke="#000" x="{x}" y="{y}" width="{szer}" height="{wys}" opacity="0.5" />')
    f.write(f'<text class="podpis" x="{x}" y="{y}">({x},{y})</text>')
f.write('</svg>')
