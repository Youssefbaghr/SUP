def inverser(chaine):
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat
    return resultat


def est_palindrome(chaine):
    gauche = 0
    droite = len(chaine) - 1
    
    while gauche < droite:
        if chaine[gauche] != chaine[droite]:
            return False
        gauche += 1
        droite -= 1
    
    return True


print(est_palindrome("RADAR"))  
