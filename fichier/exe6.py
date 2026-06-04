def compterLignes(fich):
    with open(fich, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

print(compterLignes("./fichier/data/exe4.txt"))