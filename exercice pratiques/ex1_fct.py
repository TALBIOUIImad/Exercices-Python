def signe (A,B):
    if A * B  > 0 :
        print("Meme signe.")
    else:
        print("Signe different")
        
def min (A,B):
    min = A
    if A > B :
        min = B
    return min 
def max(A,B):
    max = A
    if A < B :
        max = B
    return max 
A = float(input("Veuillez saisir la valeur de A : "))
B = float(input("Veuillez saisir la valeur de B : "))
signe(A,B)
print("Le minimum est : ",min(A,B))
print("Le maximum est : ",max(A,B))