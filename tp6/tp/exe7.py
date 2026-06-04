
def renverser_liste(liste):
    n = len(liste)
    for i in range(n // 2):
        liste[i], liste[n - 1 - i] = liste[n - 1 - i], liste[i]
    return liste

# Test
ma_liste = [1, 2, 3, 4, 5]
print("Liste originale:", ma_liste)
print("Liste renversée:", renverser_liste(ma_liste))