def cat(fich):
    with open(fich, 'r', encoding='utf-8') as f:
        for ligne in f:
            print(ligne, end='')


cat("./fichier/exe1.txt")