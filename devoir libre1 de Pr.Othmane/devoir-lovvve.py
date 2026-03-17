# on demande a l'utilisateur d'entrer l'entier n 
n = int(input("Veuillez entrer une taille impair (taille >= 15) : "))
while n % 2 == 0 or n < 15:
    n = int(input("Veuillez entrer une taille impair (taille >= 15) : "))

m = n // 2            # m : milieu des lignes
col = 2 * n - 3   # col : colonne : j
mc = col // 2     # mc : milieu des Colonnes
c = 4                 # c : constante
for i in range(n):    # lignes
    for j in range(col+1):   # colonnes
        # 1. coins
        if (i == 0 and j == 0) or (i == 0 and j == col - 1) or (i == n - 1 and j == 0) or (i == n - 1 and j == col - 1):
            print("+", end="")
        # 2. milieu des colonnes
        elif j == mc and i != m and i != m-1 and i != m+1:
            print("|", end="")
        # 3. les bordures
        elif i == 0 or i == n - 1 or j == 0 or j == col - 1:
            print("#", end="")
        # 4. milieu des lignes
        elif i == m:
            if j == mc or (j == mc - c and j == mc + c) or (j == mc // 2 or j == mc + (mc // 2)):
                print("+", end="")  
            else:
                print("-", end="")
        # 5. les quatre triangles
        # les triangles en haut
        elif i < m and (j >= mc- c+1 and j <= mc + c-1) and abs(j - mc) >= (m - 1) - i:
            print("+", end="")
        # les triangles bas
        elif i > m and (j >= mc - c+1 and j <= mc + c-1) and abs(j - mc) >= i - (m + 1):
            print("+", end="")
        # 6. les quatre diagonales
        # les diagonales en haut
        elif i < m and j == mc - (m + 3) + i:
            print("\\", end="")
        elif i < m and j == mc + (m + 3) - i:
            print("/", end="")
        # les diagonales en bas    
        elif i > m and j == mc - (m + 3) + (n - 1 - i):
            print("/", end="")
        elif i > m and j == mc + (m + 3) - (n - 1 - i):
            print("\\", end="")
        # espace    
        else:
            print(" ", end="")
    # retourner a la ligne        
    print()