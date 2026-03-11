L = int(input("Veuillez entrer le nombre des lignes de triangle : "))
for i in range(1,L+1):
    espaces = "  " * (L - i)
    etoiles = "* " * i
    print(espaces + etoiles)