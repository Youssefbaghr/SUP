liste_mots = [
    "python", "lambda", "module", "string", "script",
    "format", "object", "import", "defint", "struct",
    "return", "except", "global", "locals", "switch",
    "output", "inputs", "tables", "graphs", "client",
    "server", "socket", "thread", "packet", "stream"
]

def position(mots, x, n):
    return [m for m in mots if len(m) >= n and m[n-1] == x]


resultat = position(liste_mots, 't', 6)
print(resultat) 
