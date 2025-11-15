prix = float(input("Veuillez entrer le prix hors taxe du produit : "))
print("Choisissez la catégorie de TVA.")
print("A = 7%")
print("B = 20%")
print("C = 25%")
cat = input("Votre choix : ")
if cat.upper() == 'A':
    TTC = prix + prix * 0.07
elif cat.upper() == 'B':
    TTC = prix + prix * 0.20
elif cat.upper() == 'C':
    TTC = prix + prix * 0.25
else:
    print("Catégorie invalide. Veuillez choisir A, B ou C.")
    exit()
print("Le prix TTC de ce produit est :", format(TTC, ".2f"))
    