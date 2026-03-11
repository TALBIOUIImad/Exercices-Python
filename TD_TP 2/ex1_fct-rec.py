def GOOO(n):
    if n == 0 :
        print("GO !")
    else:
        print(n)
        GOOO(n-1)
n = int(input("Veuillez entrer la valeur de n : "))
GOOO(n)