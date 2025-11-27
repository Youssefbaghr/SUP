import numpy as np

# PARTIE 1

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

# PARTIE 2

# Qestion 3 

def valide(i,j,G):
    if len(G)>i>=0 and len(G)>j>=0 : 
        return True
    else :
        return False

# Qestion 4

def couleur(t,G):
    i,j = t
    if valide(i,j,G) : 
        return G[i][j]
    else :
        return -1
    
# Qestion 5

def list_voisins(t,G):
    i,j = t
    voisins = []
    if couleur((i+1,j),G) == couleur((i,j),G) :
        voisins.append((i-1,j))
    if couleur((i-1,j),G) == couleur((i,j),G) :
        voisins.append((i+1,j))
    if couleur((i,j+1),G) == couleur((i,j),G) :
        voisins.append((i,j-1))
    if couleur((i,j-1),G) == couleur((i,j),G) :
        voisins.append((i,j+1))
    return voisins

# QUESTION 6

def chemin(L,G):
    m=len(G)
    
    for i in range(1,m):
        if L[i] not in list_voisins(L[i-1] , G):
            return False
    return True

'''
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
'''