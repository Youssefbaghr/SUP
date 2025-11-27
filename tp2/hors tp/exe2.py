
DEFAULT_AGE =65
REMISE=0
prix_initial =100


age = int(input(" entrer votre age: "))
if age >= DEFAULT_AGE :
    REMISE = REMISE + 20
elif age <= 18 :
    REMISE = REMISE + 10
else :
    REMISE = REMISE 
    

prix_final = prix_initial - (prix_initial * REMISE / 100)
print("le prix final est de : ", prix_final)