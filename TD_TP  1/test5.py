n = int(input("Veuillez entrer un nombre positif : "))
while n < 0 :
    n = int(input("Veuillez entrer un nombre positif : "))
for i in range(1,101):
    if i % n == 0 :
        u = n
        break
print(n)  
    