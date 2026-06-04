def ajouter_contenu(fichier1, fichier2):
    with open(fichier2, 'r', encoding='utf-8') as src:
        contenu = src.read()
    with open(fichier1, 'a', encoding='utf-8') as dst:
        dst.write(contenu)

ajouter_contenu("./fichier/data/exe2.txt", "./fichier/data/fichier1.txt")