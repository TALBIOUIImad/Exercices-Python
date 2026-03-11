liste = []
for i in range(5) :
    liste.append(float(input(f"Veuillez saisir la nombre {i+1} : ")))
print("La somme des 5 nombres est : ",sum(liste))
print("La moyenne des 5 nombres est : ",format(sum(liste)/len(liste),".2f"))
