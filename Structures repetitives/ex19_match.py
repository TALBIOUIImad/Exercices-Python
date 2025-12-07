n = int(input("Veuillez saisir le nombre d'equipes participant a un championnat : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i != j :
            print("Equipe",i,"vs Equipe",j)
        else :
            continue
    