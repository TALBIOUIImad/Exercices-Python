nom_a1 = input("Veuillez entrer le nom de l'article 1 : ")
prix_a1 = float(input("Veuillez entrer le prix : "))
nom_a2 = input("Veuillez entrer le nom de l'article 2 : ")
if nom_a1 != nom_a2 :
    prix_a2 = float(input("Veuillez entrer le prix : "))
nom_a3 = input("Veuillez entrer le nom de l'article 3 : ")
if nom_a1 != nom_a3 and nom_a2 != nom_a3 :
    prix_a3 = float(input("Veuillez entrer le prix : "))
donne = float(input("Veuillez entrer le montant donne par le client : "))
q1 = 1
q2 = 1
q3 = 1
if nom_a1 == nom_a2:
    q1 += 1
    q2 = 0
if nom_a1 == nom_a3:
    q1 += 1
    q3 = 0
if nom_a2 == nom_a3 and nom_a2 != nom_a1:
    q2 += 1
    q3 = 0
if nom_a1 != nom_a2 and nom_a1 != nom_a3 and nom_a2 != nom_a3 :
    total = q1 * prix_a1 + q2 * prix_a2 + q3 * prix_a3
if nom_a1 == nom_a2 and nom_a1 != nom_a3 and nom_a2 != nom_a3 :
    total = (q1 * prix_a1) + q3 * prix_a3
if nom_a1 != nom_a2 and nom_a1 == nom_a3 and nom_a2 != nom_a3 :
    total = (q1 * prix_a1) + q2 * prix_a2 
if nom_a1 != nom_a2 and nom_a1 != nom_a3 and nom_a2 == nom_a3 :
    total = q1 * prix_a1 + (q2 * prix_a2)
if nom_a1 == nom_a2 and nom_a1 == nom_a3 and nom_a2 == nom_a3 :
    total = q1 * prix_a1
monnaie = donne - total
print("\n             Ticket de caisse :         \n")
print(f'{"Articles":<20}{"Quantite":<15}{"Prix"}')
if q1 != 0 :
    print(f'{nom_a1:<20}{q1:<15}{prix_a1:.2f}{" DHS"}')
if q2 != 0 :
    print(f'{nom_a2:<20}{q2:<15}{prix_a2:.2f}{" DHS"}')
if q3 != 0 :
    print(f'{nom_a3:<20}{q3:<15}{prix_a3:.2f}{" DHS"}')
print("\n----------------------------------------------\n")
print(f'{"Total":<35}{total:.2f}{" DHS"}')
print(f'{"Montant donne":<35}{donne:.2f}{" DHS"}')
print(f'{"Monnaie a rendre":<35}{monnaie:.2f}{" DHS"}')