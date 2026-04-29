import random
objects = []
nbr_ele = int(input("Entrer le nombre des elements : "))
for i in range(nbr_ele):
    ele = input(f"Entrer l'element {i+1} : ")
    objects.append(ele)
nbr_random = int(input("Entrer le nombre de choix parhasard : "))
while nbr_random > len(objects):
    print("Ce nombre est n'existe pas")
    nbr_random = int(input("Entrer le nombre de choix parhasard : "))
rdm = random.sample(objects,nbr_random)
print(rdm)
    