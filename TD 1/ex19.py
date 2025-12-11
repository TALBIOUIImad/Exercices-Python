s = int(input("Veuillez entrer le nombre de secondes : "))
h = s // 3600
min = (s  % 3600 ) // 60 
se = (s  % 3600 ) % 60
print(s,"seconde => ",h,"Heurs",min,"minutes",se,"secondes")