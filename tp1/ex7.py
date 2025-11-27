def convertir_secondes(total_secondes):
    SECONDES_PAR_MINUTE = 60
    SECONDES_PAR_HEURE = 60 * 60 
    SECONDES_PAR_JOUR = 24 * 60 * 60 
    SECONDES_PAR_MOIS = 30 * 24 * 60 * 60 
    SECONDES_PAR_ANNEE = 365 * 24 * 60 * 60  

    annees = total_secondes // SECONDES_PAR_ANNEE
    reste = total_secondes % SECONDES_PAR_ANNEE
    
    mois = reste // SECONDES_PAR_MOIS
    reste = reste % SECONDES_PAR_MOIS
    
    jours = reste // SECONDES_PAR_JOUR
    reste = reste % SECONDES_PAR_JOUR
    
    heures = reste // SECONDES_PAR_HEURE
    reste = reste % SECONDES_PAR_HEURE
    
    minutes = reste // SECONDES_PAR_MINUTE
    reste = reste % SECONDES_PAR_MINUTE
    
    secondes = reste
    
    return annees, mois, jours, heures, minutes, secondes


def afficher_resultat(total_secondes):
    annees, mois, jours, heures, minutes, secondes = convertir_secondes(total_secondes)
    
    print(f"\n{total_secondes:,} secondes équivalent à:")
    print(f"  → {annees} année(s)")
    print(f"  → {mois} mois")
    print(f"  → {jours} jour(s)")
    print(f"  → {heures} heure(s)")
    print(f"  → {minutes} minute(s)")
    print(f"  → {secondes} seconde(s)")

if __name__ == "__main__":
    print("=== Convertisseur de secondes ===\n")
    
    try:
        secondes_totales = int(input("Entrez le nombre de secondes à convertir: "))
        if secondes_totales < 0:
            print("Erreur: Veuillez entrer un nombre positif!")
        else:
            afficher_resultat(secondes_totales)
            
    except ValueError:
        print("Erreur: Veuillez entrer un nombre entier valide!")