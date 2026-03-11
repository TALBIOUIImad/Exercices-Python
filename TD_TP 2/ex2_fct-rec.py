def somme_int(n):
    if n == 0 :
        return 0
    return n + somme_int(n-1)
n = int(input("Veuillez entrer un nombre entier : "))
print("La somme des entiers est : ",somme_int(n))