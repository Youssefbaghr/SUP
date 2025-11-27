base = int(input("Base : "))
exposant = int(input("Exposant : "))

resultat = 1
for _ in range(exposant):
    resultat *= base

print("Résultat =", resultat)
