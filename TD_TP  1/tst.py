n = int(input("Veuillez entrer un nombre entier positif : "))
s = 0
while n <= 0 :
    n = int(input("Veuillez entrer un nombre entier positif : "))
for i in range(1,n+1) :
    s += i
print(s)