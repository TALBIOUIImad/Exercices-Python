notes = []
nbr_etud = int(input("Veuillez entrer le nombre des etudiants : "))
for i in range(nbr_etud):
    n = float(input(f'la note de etudiant {i+1} : '))
    notes.append(n)
for i,v in enumerate(notes,1):
    print("La note d'etudiant ",i," est : ",v)