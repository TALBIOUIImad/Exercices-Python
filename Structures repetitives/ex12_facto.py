n = int(input("Veuillez entrer la valeur de n (positif non nul): "))
while n < 0 :
    n = int(input("Veuillez entrer la valeur de n (positif non nul): "))
f = 1
i = 1
if n == 0 :
    print("La factorielle de 0! est : 1")    
else :
    while i <= n :
        f *= i
        i += 1
    print("La factorielle de ",n,"! est : ",f)