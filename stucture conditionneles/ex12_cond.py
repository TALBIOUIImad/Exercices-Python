annee = int (input("Veuillez saisir une annee :"))
if annee % 4 == 0 and annee % 100 != 0 or annee % 4 == 0 :
    print("L'annee ",annee," est bissextile")
else:
    print("L'annee ",annee," est non bissextile")