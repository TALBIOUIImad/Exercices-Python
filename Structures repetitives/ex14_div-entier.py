n = int(input("Veuillez entrer un nombre entier : "))
while n <= 0 :
    n = int(input("Veuillez entrer un nombre entier : "))
print("Les dividieurs de ",n," est : ")
for i in range(1,n+1) :
    if n % i  == 0 :
        print(i)