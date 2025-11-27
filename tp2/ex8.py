
EPS = 1e-12  # petite tolérance pour comparer à zéro

def solve_quadratic(a, b, c):
    """Retourne une description des solutions et la/les solutions sous forme de tuple."""
    # Cas dégénérés : a ≈ 0 => équation linéaire ou indéterminée
    if abs(a) < EPS:
        if abs(b) < EPS:
            if abs(c) < EPS:
                return ("infini", None)     # 0 = 0 : infinité de solutions
            else:
                return ("aucune", None)     # c = 0 impossible : aucune solution
        else:
            # équation linéaire bx + c = 0 -> x = -c/b
            x = -c / b
            return ("linéaire", (x,))
    # Cas quadratique propre
    d = b * b - 4 * a * c  # discriminant
    if d > EPS:
        # deux racines réelles distinctes
        sqrt_d = d ** 0.5
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        return ("deux_réelles", (x1, x2))
    elif abs(d) <= EPS:
        # racine double
        x = -b / (2 * a)
        return ("double", (x,))
    else:
        # racines complexes conjuguées
        sqrt_d = (abs(d) ** 0.5) * 1j
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        return ("deux_complexes", (x1, x2))

def main():
    print("Résolution de ax^2 + bx + c = 0")
    try:
        a = float(input("Entrez a: ").strip())
        b = float(input("Entrez b: ").strip())
        c = float(input("Entrez c: ").strip())
    except Exception:
        print("Entrée invalide. Veuillez entrer des nombres (utiliser '.' pour les décimales).")
        return

    typ, sol = solve_quadratic(a, b, c)

    if typ == "infini":
        print("Infinité de solutions (toute valeur de x convient).")
    elif typ == "aucune":
        print("Aucune solution.")
    elif typ == "linéaire":
        print("Équation linéaire. Solution unique:")
        print("x =", sol[0])
    elif typ == "deux_réelles":
        x1, x2 = sol
        print("Deux racines réelles distinctes:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif typ == "double":
        print("Racine double:")
        print("x =", sol[0])
    elif typ == "deux_complexes":
        x1, x2 = sol
        print("Deux racines complexes conjugées:")
        print("x1 =", x1)
        print("x2 =", x2)

if __name__ == "__main__":
    main()