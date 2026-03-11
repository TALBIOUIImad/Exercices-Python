n = int(input("Veuillez entrer un nombre entier positif : "))
m = int(input("Veuillez entrer un nombre entier positif : "))
if n < m :
    min = n 
else:
    min = m
for i in range(1,min+1):
    if n % i == 0 and m % i == 0 : 
        PGCD=i
print("Le PGCD de ",n," et ",m," est : ",PGCD)
        