s = 0
for i in range(1,9) :
    print("Veuillez entrer un nombre n",i," : ")
    n = int (input())
    if n < 0 :
       break
    s += n
print("La somme des nombes est : ",s)
