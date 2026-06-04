import math

def divStrict(x):
    if not isinstance(x, int) or x <= 0:
        raise ValueError("x doit etre un entier strictement positif")
    divs = set()
    for i in range(1, int(math.isqrt(x)) + 1):
        if x % i == 0:
            j = x // i
            if i != x:
                divs.add(i)
            if j != x:
                divs.add(j)
    divs_sorted = sorted(d for d in divs if d != x)
    if divs_sorted:
        print(', '.join(str(d) for d in divs_sorted))
    else:
        print()  

def somDivStrict(x):
 
    if not isinstance(x, int) or x <= 0:
        raise ValueError("x doit etre un entier strictement positif")
    total = 0
    for i in range(1, int(math.isqrt(x)) + 1):
        if x % i == 0:
            j = x // i
            if i != x:
                total += i
            if j != x and j != i:
                total += j
    return total

def amis(x, y):

    if (not isinstance(x, int) or x <= 0) or (not isinstance(y, int) or y <= 0):
        raise ValueError("x et y doivent etre des entiers strictement positifs")
    if x == y:
        return False
    return somDivStrict(x) == y and somDivStrict(y) == x


if __name__ == "__main__":
    divStrict(8)                 # affiche: 1, 2, 4
    print(somDivStrict(8))       # affiche: 7
    print(amis(284, 220))        # affiche: True