def TriComptage(tab):
    # Trouver la borne supérieure (valeur maximale du tableau)
    borneSuperieure = 0
    
    for k in tab:
        if k > borneSuperieure:
            borneSuperieure = k
    
    # Créer un tableau de comptage initialisé à zéro
    tabComptage = [0] * (borneSuperieure + 1)
    
    # Compter l'occurrence de chaque élément
    for k in tab:
        tabComptage[k] = tabComptage[k] + 1
    
    # Reconstruire le tableau trié
    tabTrie = [] 
    N = len(tabComptage)
    
    # Pour chaque valeur, l'ajouter au tableau trié autant de fois qu'elle apparaît
    for i in range(N):
        for _ in range(tabComptage[i]):
            tabTrie.append(i)
    
    return tabTrie


if __name__ == "__main__":
    numbers = [4, 2, 8, 5, 2, 8, 1, 5, 9]
    print(TriComptage(numbers))
    print(TriComptage([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))