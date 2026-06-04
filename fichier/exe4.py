def copier_lignes_commencant_par_e(fichier1, fichier2):
    with open(fichier1, 'r', encoding='utf-8') as src, open(fichier2, 'w', encoding='utf-8') as dst:
        for ligne in src:
            if ligne.startswith('e'):
                dst.write(ligne)


copier_lignes_commencant_par_e("./fichier/data/exe4.txt", "./fichier/data/exes4.txt")

