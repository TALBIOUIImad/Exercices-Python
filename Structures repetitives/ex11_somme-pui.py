n = int(input("Veuillez entrer la valeur de n : "))
s = 0
i = 0
while i <= n :
    s += 10 ** i
    i += 1
print("La somme de 10**0 + 10**1 + 10**2 + ... + 10 **",n,"est : ",s)