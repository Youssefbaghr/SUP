import math
import matplotlib.pyplot as plt


def main():
    try:
        u0 = float(input("Entrez u0 : "))
        n = int(input("Entrez un entier n >= 0 : "))
    except ValueError:
        print("Entrée invalide. Veuillez saisir un nombre réel pour u0 et un entier pour n.")
        return

    if n < 0:
        print("n doit être un entier naturel.")
        return

    X = list(range(n + 1))
    Y = [u0]

    for _ in range(n):
        Y.append(math.log(1 + Y[-1] ** 2))

    print(f"u_{n} = {Y[-1]}")
    print("Liste des indices X =", X)
    print("Liste des termes Y =", Y)

    plt.plot(X, Y, marker='o', linestyle='-')
    plt.xlabel('n')
    plt.ylabel('u_n')
    plt.title('Suite u_{n+1} = ln(1 + u_n^2)')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
