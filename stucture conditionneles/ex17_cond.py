import math
a = int(input("Veuillez entrer la valeur de A : "))
b = int(input("Veuillez entrer la valeur de B : "))
c = int(input("Veuillez entrer la valeur de C : "))
delta = (b**2) - (4 * a * c)
if delta > 0 :
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print("Les solutions de cette equation est : x1:",format(x1,".2f"),",x2:",format(x2,".2f"))
elif delta == 0 :
    x = (-b) / (2 * a)
    print("La solution de cette equation est : x: ",format(x,".2f"))
else:
    print("L´equation n´admet pas une solution ")