def supprimer_occurrences(liste, x):
    i = 0
    while i < len(liste):
        if liste[i] == x:
            liste.pop(i)
        else:
            i += 1
    return liste


def supprimer_doublons(liste):
    result = []
    for item in liste:
        if item not in result:
            result.append(item)
    return result


# Exemple d'utilisation
nombres = [1, 2, 2, 1, 4, 2, 5 ,5,1,2,45,4656,3,355,3,35,4]
x = 2

print(f"Liste avant: {nombres}")
supprimer_occurrences(nombres, x)
print(f"Liste après suppression de {x}: {nombres}")

# Test du nouveau fonction
nombres2 = [1, 2, 2, 1, 4, 2, 5 ,5,1,2,45,4656,3,355,3,35,4]
print(f"\nListe avec doublons: {nombres2}")
print(f"Liste sans doublons: {supprimer_doublons(nombres2)}")