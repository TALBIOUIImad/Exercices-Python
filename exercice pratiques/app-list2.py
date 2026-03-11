Analyse = [10,12,14.5,6,2.5]
Algebre = [8,6.5,12,14.5,10.5]
Probabilite = [9.5,14,12,15,13.5]
Statistique = [19,20,10,19,18]
Sa = Analyse + Algebre + Probabilite + Statistique
S = sum(Sa)
T =len(Sa)
print("la somme des toutes les 4 matieres est : ",format(S,".2f"))
print("le moyenne des toutes les 4 matieres est : ",format(S/T,".2f"))
print("La note maximale est : ",format(max(Sa),".2f"))
print("La note minimale est : ",format(min(Sa),".2f"))