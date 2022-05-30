def odlicz(a, b):
    if a > b:
        for x in range(b, a+1):
            print(a+b-x)
        else:
            for x in range(a, b+1):
                print(x)