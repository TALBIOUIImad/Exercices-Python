ma_list = []
for i in range(5):
    n = float(input(f'Veuillez entrer le nombre {i+1}: '))
    ma_list.append(n)
    
print("La somme des nombres est : ",sum(ma_list))
