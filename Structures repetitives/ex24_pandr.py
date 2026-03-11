n = int(input("Veuillez entrer un nombre entier : "))
N = n
inv = 0
while n != 0 :
    inv = (inv*10) + (n % 10 )
    n //= 10
if N == inv :
    print("Le nombre ",N," est palindrome.")
else:
    print("Le nombre ",N," n'est pas palindrome.")