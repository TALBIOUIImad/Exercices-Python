age = int(input("Veuillez entrer voter age : "))
sexe = input("Veuillez entrer voter sexe (H/F) : ")
if sexe == 'H' and age > 20 :
    print("Ce L´habitat est imposabe.")
elif sexe == 'F' and age >= 18  and age <= 35 :
     print("Ce L´habitat est imposabe.")
else:
    print("Ce L´habitat est non imposabe.")
    
