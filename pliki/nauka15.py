import os
import glob

for x in glob.glob('*'):
    s = os.stat(x)
    rozmiar = os.path.getsize(x)
    print(f"{x:20} {s.st_size:10}  {rozmiar:10}")

