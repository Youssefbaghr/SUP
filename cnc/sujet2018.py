import numpy as np


def ABM2(f, a, b, y0, h):
    if h <= 0:
        raise ValueError("Le pas h doit être strictement positif")
    if b <= a:
        raise ValueError("Il faut b > a")

    # Nombre de pas (on arrondit au plus proche entier)
    N = int(round((b - a) / h))
    if N < 1:
        # Si l'intervalle est plus petit que le pas, on renvoie la valeur initiale seulement
        T = np.array([a])
        Y = np.array([np.asarray(y0, dtype=float)])
        return T, Y

    # Grille des temps : de a à a + N*h inclus
    T = np.linspace(a, a + N * h, N + 1)

    # Préparer le tableau Y : gérer le cas scalaire et vecteur
    y0_arr = np.asarray(y0, dtype=float)
    y_shape = y0_arr.shape  # () pour scalaire, (k,) pour vecteur

    # Y aura pour forme (N+1, ) + y_shape si y est vectoriel
    Y = np.zeros((N + 1,) + y_shape, dtype=float)
    Y[0] = y0_arr

    # Calcul de y1 par Euler explicite
    f0 = np.asarray(f(T[0], Y[0]))
    Y[1] = Y[0] + h * f0

    # Boucle principale
    for n in range(1, N):
        tn = T[n]
        tn_1 = T[n - 1]

        fn = np.asarray(f(tn, Y[n]))
        fn_1 = np.asarray(f(tn_1, Y[n - 1]))

        # Prédicteur Adams-Bashforth 2-step
        y_pred = Y[n] + h * (1.5 * fn - 0.5 * fn_1)

        # Évaluer la dérivée au point prédit
        f_pred = np.asarray(f(T[n + 1], y_pred))

        # Correcteur Adams-Moulton (ordre 2)
        Y[n + 1] = Y[n] + 0.5 * h * (f_pred + fn)

    # Si y0 était scalaire, simplifier la forme de Y pour renvoyer vecteur 1D
    if y_shape == ():
        Y = Y.reshape((N + 1,))

    return T, Y


if __name__ == "__main__":
    # Exemple 1 : équation y' = -2*y, solution analytique y(t)=exp(-2 t)
    def f1(t, y):
        return -2.0 * y

    a, b = 0.0, 2.0
    y0 = 1.0
    h = 0.1

    T, Y = ABM2(f1, a, b, y0, h)

    print("t\ty_n\ty_exact\terreur_abs")
    for i in range(0, len(T), max(1, len(T)//10)):
        t = T[i]
        y_num = Y[i]
        y_ex = np.exp(-2.0 * t)
        print(f"{t:.3f}\t{y_num:.6f}\t{y_ex:.6f}\t{abs(y_num - y_ex):.2e}")
    print("\nErreur finale (absolue) =", abs(Y[-1] - np.exp(-2.0 * T[-1])))

