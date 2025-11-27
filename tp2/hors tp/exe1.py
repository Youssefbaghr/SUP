def ask_user_check() : 
    age = int(input(" entrer votre age: "))
    if age >= 18 :
        print("vous etes majeur")
        print("vous pouvez prendre le permis")
    else :
        print("vous etes mineur")
        print("vous ne pouvez pas prendre le permis")

ask_user_check()