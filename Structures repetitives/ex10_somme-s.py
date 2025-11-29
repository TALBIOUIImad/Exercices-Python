n = int(input("Veuillez entrer la valeur n : "))
s = 0
i = 1
while i <= n :
        s += 1/i
        i += 1
print("La somme de 1/1 + 1/2 + ... + 1/",n,"est : ",format(s,".2f"))