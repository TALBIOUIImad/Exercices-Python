n = int(input("Veuillez entrer un entier : "))
chff = 0
if n == 0 :
    chff += 1
while n != 0 :
    n //= 10 
    chff += 1
print("Le nombre total des chaiffres est : ",chff)