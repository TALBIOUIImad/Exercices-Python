import random
me = 0
pc = 0
nom = input("Veuillez entrer votre nom : ")
while True :
    print("1 . Pierre \n2 . Feuille \n3 . Ciseaux \n0 . Quitter ")
    m = int(input("Veuillez entrer votre choix : "))
    if m == 0 :
        print("Fin de jeu.")
        break
    if m not in {1,2,3} :
        print("Choix invalide.")
        continue
    choix = {1: "Pierre", 2: "Feuille", 3: "Ciseaux"}
    p = random.randint(1,3)
    if p == m :
        print("Egalite!")
    elif (p == 2 and m == 1) or (p == 3 and m == 2) or (p == 1 and m == 3):
        pc += 1
        print("Le Pc va gagne.")
    else :
        me += 1
        print("Tu as gagne.")
    print(f"{nom} a choisi : {choix[m]}")
    print(f"PC a choisi : {choix[p]}")    
    print(f'Score ===>>> {nom} : {me} | Pc : {pc}')    
    