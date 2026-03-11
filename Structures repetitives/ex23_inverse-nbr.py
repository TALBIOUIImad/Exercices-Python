n = int(input("Veuillez entrer un entier : "))
inv = 0
while n != 0 :
    inv = (inv * 10 ) + (n % 10 )
    n //= 10
print("L'inverse est : ",inv)