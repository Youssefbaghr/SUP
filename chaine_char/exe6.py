def remplacer(mot, l1, l2):
    resultat = ""
    for c in mot:
        if c == l1:
            resultat += l2
        else:
            resultat += c
    return resultat


print(remplacer("sgsgaafahcagachgacvaghvagvagvjaaajgvahjvajhvahjvajhvkajhvahajvahjvahjavhjavhagahtrafcagcjgafutafgacghafatydfahgca gfa asgasadgsdgsg" , "a" , "B"))