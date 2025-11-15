
T = int(input("Veuillez entrer un temps T (entier) : "))
h = T // 3600
min = (T % 3600) // 60
s = (T % 3600) % 60
print("T =",T," seconds => ",h," heures ",min," minutes ",s," seconds.")