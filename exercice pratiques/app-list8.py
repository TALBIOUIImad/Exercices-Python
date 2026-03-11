n_eleves = []
matier_1 = []
matier_2 = []
for i in range(5):
    print(f"L'eleve {i+1}")
    n = input("   Le nom : ")
    n_eleves.append(n)
    m_1 = float(input("   La note de matier 1 : "))
    matier_1.append(m_1)
    m_2 = float(input("   La note de matier 2 : "))
    matier_2.append(m_2)
S1 = matier_1[0] + matier_2[0]
M1 = S1 / 2
S2 = matier_1[1] + matier_2[1]
M2 = S2 / 2
S3 = matier_1[2] + matier_2[2]
M3 = S3 / 2
S4 = matier_1[3] + matier_2[3]
M4 = S4 / 2
S5 = matier_1[4] + matier_2[4]
M5 = S5 / 2
moyenne = [M1,M2,M3,M4,M5]
print(f"====> la liste des eleves <====")
for nom , m1 , m2 , m in zip(n_eleves,matier_1,matier_2,moyenne):
    print(nom,'donne a la matier 1 : ',format(m1,".2f"),'et la matier 2 : ',format(m2,".2f"),' et sa moyenne : ',format(m,".2f"))