from math import pi

def parse_float(s):
    try:
        return float(s.replace(",", "."))
    except Exception:
        raise ValueError(f"nombre invalide: {s!r}")

def volume_unifie_simple(mode, valeur, h):
    mode = mode.strip().lower()
    if mode in ("r", "rayon"):
        r = parse_float(valeur)
        if r < 0: raise ValueError("rayon doit être >= 0")
        return pi * r * r * h
    if mode in ("d", "diametre", "diameter"):
        d = parse_float(valeur)
        if d < 0: raise ValueError("diamètre doit être >= 0")
        r = d / 2.0
        return pi * r * r * h
    if mode in ("p", "perimetre", "perimeter", "circ"):
        per = parse_float(valeur)
        if per < 0: raise ValueError("périmètre doit être >= 0")
        r = per / (2 * pi)
        return pi * r * r * h
    if mode in ("a", "surface", "aire"):
        A = parse_float(valeur)
        if A < 0: raise ValueError("surface doit être >= 0")
        return A * h
    raise ValueError("mode inconnu")

def main():
    print("Calculateur de volume simple. Modes: r (rayon), d (diamètre), p (périmètre), a (surface). q pour quitter.")
    while True:
        mode = input("Mode (r/d/p/a) > ").strip()
        if mode.lower() == "q":
            break
        try:
            val = input("Valeur (selon le mode) > ").strip()
            if val.lower() == "q": break
            h_s = input("Hauteur h > ").strip()
            if h_s.lower() == "q": break
            h = parse_float(h_s)
            if h < 0:
                print("Erreur: hauteur doit être >= 0")
                continue
            v = volume_unifie_simple(mode, val, h)
            print(f"Volume = {v}")
        except Exception as e:
            print("Erreur:", e)

if __name__ == "__main__":
    main()
