def analyse_notes(notes_m: dict):
    s = 0
    print("\n ==> Notes de l'etudiant <== \n")
    for mat ,note in notes_m.items():
        print(f"{mat} : {note}")
        s += note
    m = s / len(notes_m)
    print("La moyenne des notes est : ",m)
    if m >= 10 :
        print("Admis")
    else:
        print("Ajourne")
nbr_m = int(input("Veuillez entrer le nombre de matier : "))
notes_m = {}
for i in range(nbr_m):
    matier = input(f"Veuillez entrer le nom de la matier {i+1}: ")
    note_m = float(input(f"Veuillez entrer la note de {matier} (sur 20) : "))
    notes_m[matier] = note_m
analyse_notes(notes_m)
