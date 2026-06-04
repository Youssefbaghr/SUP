def dict_occ(mot):
    return {c: mot.count(c) for c in set(mot)}

print(dict_occ("langage"))