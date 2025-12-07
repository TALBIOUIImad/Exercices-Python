import random
p = random.randint(1,30)
rep = 5
while rep > 0 :
    rep -= 1
    n = int(input("Entrer un nombre : "))
    if n < p :
        print("Trop petit.")
    elif n > p :
        print("Trop grand.")
    else :
        break
if rep != 0 :
     print("Vous savez trouve le nombre ! en",(5-rep),"tentative.")
else :
    print("Vous savez depasse les 5 tentatives. le nombre etait : ",p)