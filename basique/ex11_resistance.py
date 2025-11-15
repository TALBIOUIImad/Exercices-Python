R1 = float(input("Vieullez entrer la valeur de la resistance R1 : "))
R2 = float(input("Vieullez entrer la valeur de la resistance R2 :  "))
R3 = float(input("Vieullez entrer la valeur de la resistance R3 :  "))
Rs = R1 + R2 + R3
Rp = (R1*R2*R3) / (R1*R2+R1*R3+R2*R3)
print("Si les resistances branchees en serie : ",format(Rs,".2f"))
print("Si les resistances branchees en parallele : ",format(Rp,".2f"))