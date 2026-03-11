m = input("Veuillez entrer un mote : ")
n= list(m)
M = n.copy()
n.reverse()
print(M)
print(n)
if n == M :
    print(f"le mote {m} est palandrome ")
else:
    print(f"le mote {m} n'est pas palandrome ")