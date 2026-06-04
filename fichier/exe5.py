def compterMots(fich):
    compteur = 0
    with open(fich, 'r', encoding='utf-8') as f:
        for ligne in f:
            mots = ligne.split()
            compteur += len(mots)
    return compteur


print(compterMots("./fichier/data/exe4.txt"))

