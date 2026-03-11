def factorielle(n):
    if n == 0 :
        return 1
    return n * factorielle(n-1)
n = int(input("Veuillez entrer un nombre entier : "))
print("La factorielle de ",n," est : ",factorielle(n))