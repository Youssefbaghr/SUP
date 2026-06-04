import random

def liste_alea(n):
    return [random.randint(0, 20) for i in range(n)]

print(liste_alea(10))
