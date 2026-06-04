def f4(d):
    return {k: sum(v)/len(v) for k, v in d.items()}

d = {
    "etudiant1": [14, 16, 18],
    "etudiant2": [12, 15, 17],
    "etudiant3": [16, 16, 13]
}

print(f4(d))