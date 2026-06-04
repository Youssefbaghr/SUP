def produit_scalaire(u, v):
    if len(u) != len(v):
        raise ValueError("Les vecteurs doivent avoir la même dimension")
    
    return sum(u[i] * v[i] for i in range(len(u)))

if __name__ == "__main__":
    u = [1, 2, 3]
    v = [4, 5, 6]
    
    resultat = produit_scalaire(u, v)
    print(f"Vecteur U: {u}")
    print(f"Vecteur V: {v}")
    print(f"Produit scalaire: {resultat}")