dic = {}
nom = input("Veuillez entrer votre nom : ")
dic['nom'] = nom
prenom = input("Veuillez entrer votre prenom : ")
dic['prenom'] = prenom
age = int(input("Veuillez entrer votre age : "))
dic['age'] = age
filier = input("Veuillez entrer votre filier : ")
dic['filier'] = filier
print(dic)
print(dic.keys())
print(dic.values())