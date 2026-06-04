def suppression(c, s):
    index = s.find(c)
    if index == -1:
        return s
    return s[:index] + s[index + 1:]

# TEST  

print(suppression('a', "banana"))  # "bnna"
print(suppression('x', "banana"))  # "banana"

def scrabble(mot, lettres_disponibles):
    for caractere in mot:
        if caractere not in lettres_disponibles:
            return False
        lettres_disponibles = suppression(caractere, lettres_disponibles)
    return True


# TEST  

print(scrabble("chat", "hvvcwwahht"))  # False
print(scrabble("chat", "tacb"))  # True

