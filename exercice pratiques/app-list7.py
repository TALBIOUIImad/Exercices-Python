L= []
for i in range(5):
    n = int(input(f"Veuillez entrez l'entier num {i+1} : "))
    L.append(n)
max = 0
for n in L :
    if n > max :
        max = n 
print("Le maximum est ",max)