def liste_suffixes(S):
    result = []
    for p in range(len(S)):
        suffix = S[p:]
        result.append([suffix, p])
    return result

# TEST
print(liste_suffixes("abc"))  # [['abc', 0], ['bc', 1], ['c', 2]]