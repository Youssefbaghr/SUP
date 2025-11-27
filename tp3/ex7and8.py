def dessiner_etoiles():
    mode = input("Choisir mode (1: 10 '*' par ligne, 2: triangle): ").strip()
    n_str = input("Nombre de lignes: ").strip()
    if not n_str.isdigit():
        return
    n = int(n_str)
    if mode == "1":
        for _ in range(n):
            for _ in range(10):
                print("*", end="")
            print()
    elif mode == "2":
        for i in range(1, n + 1):
            for _ in range(i):
                print("*", end="")
            print()

if __name__ == "__main__":
    dessiner_etoiles()