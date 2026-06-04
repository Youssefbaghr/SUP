
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    
def produit(k):
    if k == 0:
        return 1
    else:
        return (2*k + 1) * produit(k - 1)
    
def termes(n):
    if n == 0:
        return 1
    else:
        return fact(n) / produit(n)
    
def list_termes(n):
    return [termes(k) for k in range(n + 1)]

def somme(L):
    if not L:
        return 0
    else:
        return L[0] + somme(L[1:])

    
def pi_euler(n):
    return 2 * somme(list_termes(n))

print(pi_euler(10))