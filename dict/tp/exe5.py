Temperature = {"France": [6, 5, 7, 10, 14, 18, 22, 21, 18, 13, 9, 8],
               "Australie": [35, 34, 32, 28, 24, 20, 19, 21, 25, 28, 31, 30]}

Mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]


def temp_fevrier_france():
    print("France février", Temperature["France"][1])


def AfficheMois(mois, Temperature, Mois):
    i = Mois.index(mois)
    for pays in Temperature:
        print(pays, mois, Temperature[pays][i])


def AjoutPays(Temperature, pays, liste):
    Temperature[pays] = liste


def ModificationPaysMois(pays, mois, valeur, Temperature, Mois):
    i = Mois.index(mois)
    Temperature[pays][i] = valeur


temp_fevrier_france()
AfficheMois("Janvier", Temperature, Mois)
AjoutPays(Temperature, "Brésil", [25, 25, 24, 23, 22, 21, 21, 22, 23, 24, 25, 25])
ModificationPaysMois("France", "Janvier", 8, Temperature, Mois)
print(Temperature["France"][0])