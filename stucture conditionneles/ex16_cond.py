N1 = float(input("Veuillez saisir la note 1 (sur 20) : "))
N2 = float(input("Veuillez saisir la note 2 (sur 20) : "))
N3 = float(input("Veuillez saisir la note 3 (sur 20) : "))
s = N1 + N2 + N3
m = s / 3
if m < 10 :
    print("Le moyenne des notes est : ",format(m,".2f")," avec sa montion insuffisant.")
elif 10 <=m<12 :
    print("Le moyenne des notes est : ",format(m,".2f")," avec sa montion passable.")
elif 12<=m<14 :
    print("Le moyenne des notes est : ",format(m,".2f")," avec sa montion assez bien.")
elif 14<=m<16 :
    print("Le moyenne des notes est : ",format(m,".2f")," avec sa montion bien.")
else:
    print("Le moyenne des notes est : ",format(m,".2f")," avec sa montion tres bien.")