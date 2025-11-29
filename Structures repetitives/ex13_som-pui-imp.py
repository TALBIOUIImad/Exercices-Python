n = int(input("Veuillez entrer un nombre entier : "))
j = 1
s = 0 
for i in range(1,n+1) : 
    s += j ** 2
    j += 2
print("La somme des carrees des",n,"premiers entiers impairs : ",s) 