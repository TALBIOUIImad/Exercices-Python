M = {'bois','acier','beton','verre','platre'}
print(M)
d = input("Veuillez entrer un materiau : ")
if d in M :
    print("Le materiau est disponible.")
else:
    print("Le materiau n'est pas disponible.")
M.update(['cuivre','aluminium','fer'])
for jiit in M :
    print(jiit)
#je supp verre 
M.remove("verre")
print(M)