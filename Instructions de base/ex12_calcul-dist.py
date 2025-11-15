import math
print("Vieullez entrer les cordonnees de A :")
ax = float(input(" X : "))
ay = float(input(" Y : "))
print("Vieullez entrer les cordonnees de B :")
bx = float(input(" X : "))
by = float(input(" Y : "))
# Calcul de la distance
D = math.sqrt(((bx - ax)**2) + ((by - ay)**2))
print("La distance entre A et B est : ",format(D,".2f"))