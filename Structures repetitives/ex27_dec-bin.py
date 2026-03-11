d = int(input("Veullez entrer un nombre decimal : "))
D = d
b = 0
p = 0
r = 0
ordd = 0
while d != 0 :
    r = d % 2 
    p = 10 ** ordd
    b += r * p
    ordd += 1
    d //= 2
print("Le nombre ",D," en binaire est : ",b)