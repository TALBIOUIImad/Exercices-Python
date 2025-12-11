ht = float(input("Veuillez entrer le prix Hors Taxe : "))
t = float(input("Veuillez entrer le taux de TVA en pourcentage : "))
print("\nLe detail joliment formate : \n")
print("Le montant de TVA est : ",ht * t/100,"\nLe prix TTC est : ",ht + (ht * t/100),"DHS.")
