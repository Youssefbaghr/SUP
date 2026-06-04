def copier_lignes_commencant_par_e(fichier1, fichier2):
    """Copie dans fichier2 les lignes de fichier1 qui commencent par 'e'."""
    with open(fichier1, 'r', encoding='utf-8') as src, open(fichier2, 'w', encoding='utf-8') as dst:
        for ligne in src:
            if ligne.startswith('e'):
                dst.write(ligne)
