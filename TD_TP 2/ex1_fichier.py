ma_liste = []
with open("notes.txt","r") as f :
    for ligne in f :
        ligne = ligne.strip()
        if ligne != "":
            l = int(ligne)
        ma_liste.append(l)
taille = len(ma_liste)
moyenne = sum(ma_liste)/len(ma_liste)
maximale = max(ma_liste)
minimale = min(ma_liste)
print(taille)
print("La note moyenne est : ",moyenne)
print("La note maximale est : ",maximale,"\nLa note minimale est : ",maximale)
with open("resultat.txt","w") as f :
    f.write(taille)
    f.write(moyenne)
    f.write(maximale)
    f.write(minimale) 