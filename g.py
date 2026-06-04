import matplotlib.pyplot as plt


def afficher_convergence():
    nmax = 20
    termes = [10]
    for _ in range(nmax):
        termes.append(0.5 * termes[-1] + 50)

    plt.plot(termes, 'o-')
    plt.axhline(y=100, color='r', linestyle='--', label='Limite = 100')
    plt.xlabel("Rang n")
    plt.ylabel("Terme de la suite")
    plt.title("Convergence vers la limite")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    afficher_convergence()
