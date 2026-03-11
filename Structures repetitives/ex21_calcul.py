while True :
    print("\n  =========== Calculatrice : MENU ===========\n")
    print("1 - Addition. \n2 - Soustraction. \n3 - Multiplication. \n4 - Division. \n5 - Reste d'une division entier. \n6 - Puissance. ")
    n = int(input("Quel calcul veux-tu effectuer ? : "))
    if n == 1 :
        p = float(input("Taper le premier terme : "))
        d = float(input("Taper le deuxieme terme : "))
        r = p + d 
        print("Le resultat est : ",r)
    elif n == 2 :
        p = float(input("Taper le premier terme : "))
        d = float(input("Taper le deuxieme terme : "))
        r = p - d 
        print("Le resultat est : ",r)
    elif n == 3 :
        p = float(input("Taper le premier terme : "))
        d = float(input("Taper le deuxieme terme : "))
        r = p * d 
        print("Le resultat est : ",r)
    elif n == 4 :
        p = float(input("Taper le premier terme : "))
        d = float(input("Taper le deuxieme terme : "))
        if d != 0 :
            r = p / d
            print("Le resultat est : ",r) 
        else:
            print("La division sur 0 est impossible!")
    elif n == 5 :
        p = float(input("Taper le premier terme : "))
        d = float(input("Taper le deuxieme terme : "))
        if d != 0 :
            r = p % d
            print("Le resultat est : ",r)
        else:
            print("La division sur 0 est impossible!")
    elif n == 6 :
        p = float(input("Taper le terme : "))
        d = float(input("Taper le puissance : "))
        r = p ** d 
        print("Le resultat est : ",r)
    else :
        print("Le nombre incorrect!")
    q = input("Veux-tu faire un autre calcul (Y/N) : ")
    if q == 'n' or q == 'N' :
        break