# PROBLEME : Simulation d'une caisse automatique

while True:
    prix = float(input("Entrer premier prix (0 pour arrêter) : "))

    if prix == 0:
        print("Fin du programme.")
        break   # on arrête totalement

    total = prix

    # saisie des autres produits
    while True:
        p = float(input("Entrer prix suivant (-1 pour terminer facture) : "))
        if p == -1:
            break
        total += p

    # application des réductions
    if total > 500:
        total_paye = total * 0.85
    elif total > 200:
        total_paye = total * 0.90
    elif total > 100:
        total_paye = total * 0.95
    else:
        total_paye = total

    print("Montant à payer =", total_paye)

    # paiement
    verse = float(input("Somme versée : "))
    if verse < total_paye:
        print("Paiement refusé")
    else:
        print("Monnaie à rendre :", verse - total_paye)

    print("---- Nouvelle facture ----")
