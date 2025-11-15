x = int (input("Veuillez entrer le nombre de photocopies : "))
if x <= 10 :
    prix = 0.30 * x 
elif x <= 30 :
    prix = (0.30 * 10) + ((x-10) * 0.25)
else :
    prix = (10 * 0.3) + (20 * 0.25) + ((x-30) * 0.2)   
print("La facture correspondante est : ",format(prix,".2f"),"DH")