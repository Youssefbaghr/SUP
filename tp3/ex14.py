import random
import sys

#!/usr/bin/env python3

def ask_mode():
    modes = {"e": "easy", "m": "med", "h": "hard"}
    prompt = "Choisissez un mode — easy (e), med (m) ou hard (h): "
    while True:
        choice = input(prompt).strip().lower()
        if choice in modes:
            return modes[choice]
        if choice in modes.values():
            return choice
        print("Mode invalide. Tapez e, m, h ou easy, med, hard.")

def ask_positive_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v > 0:
                return v
            print("Veuillez entrer un entier strictement positif.")
        except ValueError:
            print("Entrée invalide. Entrez un entier.")

def generate_pair(mode, med_max=None):
    if mode == "easy":
        a = random.randint(0, 9)
        b = random.randint(0, 9)
    elif mode == "med":
        a = random.randint(0, med_max)
        b = random.randint(0, med_max)
    else:  # hard
        a = random.randint(-1_000_000, 1_000_000)
        b = random.randint(-1_000_000, 1_000_000)
    return a, b

def main():
    print("Jeu de sommes — gagnez 1000 points par bonne réponse.")
    mode = ask_mode()
    rounds = ask_positive_int("Nombre de tours à jouer: ")
    med_max = None
    if mode == "med":
        med_max = ask_positive_int("Valeur maximale (>=0) pour les nombres en mode med: ")

    score = 0
    for turn in range(1, rounds + 1):
        a, b = generate_pair(mode, med_max)
        try:
            answer = input(f"[Tour {turn}/{rounds}] {a} + {b} = ")
            user_val = int(answer.strip())
        except ValueError:
            print("Entrée non entière. Fin du jeu.")
            print(f"Score final: {score}")
            sys.exit(0)

        correct = a + b
        if user_val == correct:
            score += 1000
            print(f"Correct ! Score: {score}")
        else:
            print(f"Faux. Réponse correcte: {correct}")
            print(f"Score final: {score}")
            break
    else:
        # bouclé tous les tours sans erreur
        print(f"Terminé ! Score final: {score}")

if __name__ == "__main__":
    main()