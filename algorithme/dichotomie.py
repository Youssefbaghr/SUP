def recherche_dichotomique(liste, cible):
    if not liste:
        return -1
    
    liste_triee = []
    for element in liste:
        inserted = False
        for i in range(len(liste_triee)):
            if element < liste_triee[i]:
                liste_triee.insert(i, element)
                inserted = True
                break
        if not inserted:
            liste_triee.append(element)
    print(f"Liste triée: {liste_triee}")

    gauche = 0
    droite = len(liste_triee) - 1
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        valeur_milieu = liste_triee[milieu]
        
        if valeur_milieu == cible:
            return liste.index(cible)
        elif valeur_milieu < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    
    return -1

nombres = [15,  37, 5,5, 7, 39, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95,  131, 133, 135, 137, 139, 141, 143, 145, 41, 43, 45, 47, 1, 9, 3, 13, 11, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35,49 ,97,99 , 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 51, 53, 55, 57, 59, 61, 147, 149]
resultat = recherche_dichotomique(nombres, 5)
print(f"Index: {resultat}")

mots = ["zebra", "apple","app", "mango", "banana", "grape", "orange","blueberry", "watermelon", "pineapple", "avocado", "papaya", "coconut", "fig",  "kiwi", "peach", "strawberry",  "raspberry", "blackberry"]
resultat2 = recherche_dichotomique(mots, "fig")
print(f"Index mot: {resultat2}")