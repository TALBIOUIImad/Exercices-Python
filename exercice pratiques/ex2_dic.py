resultats = {}
reussi = 0
nbr_etud = int(input("Veuillez saisir le nombre des etudiants : "))
for i in range(nbr_etud):
    print(f"L'etudiant {i+1} : ")
    nom = input("   Nom : ")
    note = float(input("   Note : "))
    resultats[nom] = note 
for nom,note in resultats.items():
    print("L'etudiant ",nom," a obtenu une note de ",note)
for nom,note in resultats.items():
    if note >= 12 :
        reussi += 1
        print(nom," a reussi avec ",note)
print("Le nombre total d'etudiants ayant reussi l'examen est : ",reussi)