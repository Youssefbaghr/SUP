def tous_distincts(L):
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] == L[j]:
                return False
    return True


# Exemples d'utilisation
print(tous_distincts([1, 2, 3, 4]))        # True
print(tous_distincts([1, 2, 3, 2]))        # False
print(tous_distincts(['a', 'b', 'c']))     # True
print(tous_distincts(['a', 'b', 'a']))     # False
