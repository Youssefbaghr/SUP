
def classify(note: float) -> str:
    if note < 10:
        return "Non valide (ajourné)"
    if 10 <= note < 12:
        return "Passable"
    if 12 <= note < 14:
        return "Assez bien"
    if 14 <= note < 16:
        return "Bien"
    return "Très bien"  

def main():
    try:
        note = eval(input("Entrez la note (0-20) : "))
    except ValueError:
        print("Entrée invalide : ce n'est pas un nombre.")
        return
    if not (0 <= note <= 20):
        print("Note hors intervalle [0, 20].")
        return
    print(f"Note = {note} -> {classify(note)}")

if __name__ == "__main__":
    main()