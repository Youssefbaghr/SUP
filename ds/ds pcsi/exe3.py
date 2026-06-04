# Version récursive
def count_recursive(L, element):
    if not L:
        return 0
    return (1 if L[0] == element else 0) + count_recursive(L[1:], element)


# Version itérative
def count_iterative(L, element):
    count = 0
    for item in L:
        if item == element:
            count += 1
    return count


# Exemples d'utilisation
L = [1, 2, 3, 2, 4, 2, 5]
print(count_recursive(L, 2))      # Résultat: 3
print(count_iterative(L, 2))      # Résultat: 3