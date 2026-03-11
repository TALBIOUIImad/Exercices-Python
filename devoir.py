n = int(input("Veuillez entrer une taille impair (taille >= 15) : "))
while n % 2 == 0 or n < 15 : 
    n = int(input("Veuillez entrer une taille impair  (taille >= 15) : "))
m = n // 2 #m : milieu 
c = 4 # c : constante
#colonnes
for i in range(n):
    #lignes
    for j in range(n):
        if (i == 0 and j == 0) or (i == 0 and j == n-1) or (i == n-1 and j == 0) or (i == n-1 and j == n-1) :
            print("+", end="")
        elif j == m  and i != m-1 and i != m+1 and i != m :
            print("|",end="")
        elif i == 0 or i == n-1 or j == 0 or j == n-1 and (i == m or j == n-1 ) :
            print("#", end="")
        elif i == m and (j == m // 2 or j == m or j == m + (m//2)):
            print("+", end="")
        elif (i == m - 1 or i == m + 1) and ((j >= m//2 and j <= m + m//2)):
            print("+", end="")
        elif i == m :
            print("-", end="")
        elif i < m and ((j >= m-c and j - m <= i - m) or (j <= m+c and j - m >= m - i)):
            print("+", end="")
        elif i > m and ((j >= m-c and j - m <= m - i) or (j <= m+c and j - m >= i - m)):
            print("+", end="")
        elif (i < m and j + c == m - (m - i - 1)) or (i > m and j - c == m + (i - m - 1)):
            print("\\",end="")
        elif (i < m and j - c == m + (m - i - 1)) or (i > m and j + c == m - (i - m - 1)):
            print("/",end="")
        else:
            print(" ", end="")    
    print()