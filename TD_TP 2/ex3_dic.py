def afficher_panier(panier: list):
    print(panier)
    s = 0
    for produit in panier :
        s += produit["prix"] * produit["Quantite"]
        print(f"{produit["nom"]} ==> {produit["prix"]} * {produit["Quantite"]}")
    print("Le prix total a payer : ",format(s,".2f")," DHS")
def produit_plus_cher(panier: list):
    p_cher = panier[0]
    for p in panier:
        if p["prix"] > p_cher["prix"]:
            p_cher = p
    print(f"Le produit le plus cher est : {p_cher["nom"]} -> {p_cher["prix"]} DHS")
panier = [] 
nbr_p = int(input("Veuillez entrer le nombre de produits a acheter : "))
for i in range(nbr_p):
    nom_p = input(f"Nom du produit {i+1} : ")
    prix = float(input(f"Prix unitaire de {nom_p} : "))
    quant = int(input(f"Quantite de {nom_p} : "))
    produit = {"nom":nom_p, "prix": prix, "Quantite": quant}
    panier.append(produit)
afficher_panier(panier)
produit_plus_cher(panier)