SECRET_CODE = 47

TENTA = 5

while TENTA > 0:
    guess = int(input("Entrez votre proposition (entre 1 et 100) : "))
    if guess == SECRET_CODE:
        print("Félicitations ! Vous avez trouvé le code secret.")
        break
    else:
        TENTA -= 1
        print(f"Proposition incorrecte. Il vous reste {TENTA} essais.")
else:
    print(f"Désolé, vous avez utilisé tous vos essais. Le code secret était {SECRET_CODE}.")