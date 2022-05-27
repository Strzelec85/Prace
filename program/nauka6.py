# https://docs.python.org/3/library/argparse.html

import argparse

parser = argparse.ArgumentParser(description="Nasz super program")
parser.add_argument('--min', default=1, type=int, help='najmniejsza wartosc')
parser.add_argument('--max', default=10, type=int, help='najwieksza wartosc')
parser.add_argument('--od', dest='min', type=int)
parser.add_argument('--krok', default=1, type=int, help='krok')
parser.add_argument('--nowelinie', action='store_const', const=True, dest='nl')

args = parser.parse_args()

od, do, krok, nl = args.min, args.max, args.krok, args.nl

for i in range(od, do+1, krok):
    print(f"{i} ", end=("\n" if nl else " ") )
