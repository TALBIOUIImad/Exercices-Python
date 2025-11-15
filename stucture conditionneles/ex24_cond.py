x = input("Veuillez entrer un caracter : ")
if "a" <= x <= "z" or "A" <= x <= "Z" :
    print("Le caractere est un alpabet")
elif "0" <= x <= "9" :
    print("Le caractere est un nombre")
else:
    print("Le caractere est un caractere special")