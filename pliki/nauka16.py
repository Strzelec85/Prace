import os

for n in range(1,20):
    nazwabazowa = f"nauka{n:02d}"
    print(f"{nazwabazowa}: ", end="")
    for rozsz in 'py', 'txt', 'dat':
        nazwapliku = f"{nazwabazowa}.{rozsz}"
        #print(nazwapliku, end=" ")
        if os.path.exists(nazwapliku):
            print(rozsz, end=" ")
        else:
            print("--", end=" ")
    print()
