import numpy as np

matrice_G = np.random.choice([0, 1], size=(10, 10)).astype(float)

# Question 1 a
def copier_matrice(matrice):
    nb_lignes, nb_colonnes = matrice.shape
    copie = np.zeros((nb_lignes, nb_colonnes))
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            copie[i, j] = matrice[i, j]
    return copie

# Question 1 b
def echanger_lignes(matrice, i, j):
    matrice[[i, j]] = matrice[[j, i]]
    return matrice

# Question 1 c
def choix_pivot(matrice, k):
    m = len(matrice)
    for i in range(k + 1, m):
        if matrice[i, k] != 0:
            return i
    return -1

def triangulaire(matrice):
    n = len(matrice)
    k = 0
    
    for i in range(n):
        pivot = choix_pivot(matrice, i)
        if pivot == -1:
            return -1
        
        echanger_lignes(matrice, i, pivot)
        k += 1
        
        for j in range(i + 1, n):
            if matrice[i, i] != 0:
                matrice[j] = matrice[j] - (matrice[j, i] / matrice[i, i]) * matrice[i]
    
    return k

# Question 1 d
def determinant(G):
    C = copier_matrice(G)
    k = triangulaire(C)
    if k == -1:
        return 0
    
    diag = np.prod(np.diag(C))
    d = diag * ((-1) ** k)
    return d

# Tests
print("Matrice G :")
print(matrice_G)
print("\nCopie de la matrice G :")
matrice_copie = copier_matrice(matrice_G)
print(matrice_copie)
print("\nÉchange des lignes 0 et 1 :")
print(echanger_lignes(matrice_copie, 0, 1))
k = triangulaire(matrice_copie)
print(f"\nMatrice triangulaire : {k}")
print(f"\nDéterminant de la matrice G : {determinant(matrice_G)}")
