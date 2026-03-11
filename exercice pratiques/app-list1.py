P =['Maroc','Algerie','Tunisie','Mali','France']
print(f'Veuillez choisir 2 de ces 5 pays : \n{P}')
n= input("le premier pays : ")
m= input("le deuxieme pays : ")
N = P.index(n)
M = P.index(m)
P[N],P[M] = P[M],P[N]
print(P)