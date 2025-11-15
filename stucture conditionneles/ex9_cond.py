a =int (input("Veuillez entrer un nombre entier : "))
b =int (input("Veuillez entrer un nombre entier : "))
op = input("Choisir une operateur : ")
if op == '+' :
    print("La somme de ",a," et ",b," est : ",a+b)
elif op == '*' :
     print("Le produit de ",a," et ",b," est : ",a*b)
elif op == '-' :
     print("La soustraction de ",a," et ",b," est : ",a-b)
elif op == '/' :
    if b != 0 :
     print("La division de ",a," et ",b," est : ",a/b)
    else:
        print("La division par 0 est impossible.")
else :
    print("L'operateur est incorrect.")