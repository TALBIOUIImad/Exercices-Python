e = int(input("Veuillez entrer un nombre entier : "))
while e <= 1 :
    e = int(input("Veuillez entrer un nombre entier : "))    
s = 0
i = 1
while i <= e :
        s += i
        i += 1
print("La somme des entier jusqu'a ",e," est : ",s)
