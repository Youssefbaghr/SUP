import random

L10 = [random.randint(1, 1000) for _ in range(10)]

def appartient(element, liste):
    for indice, item in enumerate(liste):
        if item == element:
            return indice
        return None

# Test de la fonction
print("Liste L10:", L10)
print(f"Indice de 50", appartient(50,L10))
