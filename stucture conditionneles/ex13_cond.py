A = float(input("Veuillez entrer un nombre A :"))
B = float(input("Veuillez entrer un nombre B :")) 
if A * B  > 0 :
    A,B = B,A
    print("La nouvelle valeur de A est :",A)
    print("La nouvelle valeur de B est :",B)
else :
    p = A * B 
    s = A + B
    A = s
    B = p
    print("La nouvelle valeur de A est :",A)
    print("La nouvelle valeur de B est :",B)
  
    