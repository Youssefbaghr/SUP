def copie_en_majuscules(fichier1, fichier2):
    with open(fichier1, 'r', encoding='utf-8') as src:
        contenu = src.read()
    with open(fichier2, 'w', encoding='utf-8') as dst:
        dst.write(contenu.upper())


copie_en_majuscules("./fichier/data/exe4.txt", "./fichier/data/exe7.txt")