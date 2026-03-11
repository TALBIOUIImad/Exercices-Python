n = int(input("Veuillez entrer un nombre (entre 1 et 9  ) : "))
while n < 1 or n > 9 :
    n = int(input("Veuillez entrer un nombre (entre 1  et 9  ) : "))
i = 0
while i <= 9 :
    print(i," * ",n," = ",i*n)
    i +=1
