# Exercice 4 : tester si un nombre est premier
N = int(input("Entrer un entier > 1 : "))
est_premier = True

for d in range(2, N):
    if N % d == 0:
        est_premier = False
        break

if est_premier:
    print("Nombre premier")
else:
    print("Non premier")