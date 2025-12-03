n = int(input("Veuillez entrer la valeur de n : "))
while n < 2 :
    n = int(input("Veuillez entrer la valeur de n : "))
u0 = 0
u1 = 1
print("Les termes de la suite de fibonacci sont : "  )
print(u0)
print(u1)
for i in range(n-1) :
    u = u1 + u0
    print(u)
    u0 = u1
    u1 = u