def matrice_to_vecteur(M):
    V = []
    for ligne in M:
        for element in ligne:
            V.append(element)
    return V


def somme_matrices(M1, M2):
    if len(M1) != len(M2) or len(M1[0]) != len(M2[0]):
        return "Erreur: les matrices doivent avoir les mêmes dimensions"
    
    resultat = []
    for i in range(len(M1)):
        ligne = []
        for j in range(len(M1[0])):
            ligne.append(M1[i][j] + M2[i][j])
        resultat.append(ligne)
    return resultat


def produit_matrices(M1, M2):
    if len(M1[0]) != len(M2):
        return "Erreur: nombre de colonnes de M1 doit égaler nombre de lignes de M2"
    
    resultat = []
    for i in range(len(M1)):
        ligne = []
        for j in range(len(M2[0])):
            somme = 0
            for k in range(len(M2)):
                somme += M1[i][k] * M2[k][j]
            ligne.append(somme)
        resultat.append(ligne)
    return resultat


# Exemple d'utilisation
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

M2 = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 1]
]

V = matrice_to_vecteur(M)
print(f"Matrice: {M}")
print(f"Vecteur: {V}")
print(f"\nSomme: {somme_matrices(M, M2)}")
print(f"Produit: {produit_matrices(M, M2)}")