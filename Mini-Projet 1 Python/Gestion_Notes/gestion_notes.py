#fcts des validation des notes et calcul moyenne et total et gestion des index
    #dic qui associe chaque module a ses position dans treeview ({"Algèbre 1": (4, 5)} == note de algebre 1 dans colonne 4 et le coef de alg1 dans colonne 5)
INDEX_MODULES = {"Algèbre 1": (4, 5),"Analyse 1": (6, 7),"MTU": (8, 9),"P. Python": (10, 11),"Algorithmique et p. C": (12, 13),"Architecture fonctionnement des ordinateurs": (14, 15),"Électronique numérique": (16, 17)}

    #retourne le tuple (index_note,index_coeff) d'un module pour placer dans treeview  
def get_index(module):
    return INDEX_MODULES[module]

    #retourne le dic complet des index (utiliser pour parcourir tous les modules)
def get_all_index():
    return INDEX_MODULES

    #valide la saisie d'une note avec les regles suivants
def valider_note(text_actuel):
    if text_actuel == "":
        return True
    if text_actuel == ".":         
        return True
    if text_actuel.count(".") > 1:
        return False
    if "." in text_actuel:
        apres_point = text_actuel.split(".")[1]
        if len(apres_point) > 2:
            return False
    try:
        nbr = float(text_actuel)
        if nbr > 20:
            return False
        if nbr < 0:
            return False
        return True
    except:
        return False

    #verifier si tous les notes sont saisires et calcule de total et moyenne d'un etudiant sa montion selon sa moyenne
def calculer_total_moyenne(valeurs):
    #verifier si tous les notes sont remplies
    tous_remplis = True
    for module in INDEX_MODULES:
        idx_n, idx_c = INDEX_MODULES[module]
        if str(valeurs[idx_n]) == "":
            tous_remplis = False
            break
    if not tous_remplis:
        return None
    Total = 0
    Total_coef = 0
    #calculer la somme des coefs et total des notes  
    for module in INDEX_MODULES:
        idx_n, idx_c = INDEX_MODULES[module]
        Total += float(valeurs[idx_n]) * int(valeurs[idx_c])
        Total_coef += int(valeurs[idx_c])
    #calculer moyenne 
    Moyenne = float(format(Total / Total_coef,".2f"))
    Total = float(format(Total,".2f"))
    #determiner la montion selon la moyenne
    if Moyenne < 10:
        Mention = "N.validé"
    elif Moyenne < 12:
        Mention = "Admis"
    elif Moyenne < 14:
        Mention = "A.bien"
    elif Moyenne < 16:
        Mention = "Bien"
    else:
        Mention = "T.bien"
    return {"Total": Total,"Moyenne": Moyenne,"Mention": Mention}

    #retourne la liste des modules dont la note n'a pas encore ete saisire pour un etudiant (utiliser dans combobox des notes)
def get_modules_restants_etudiant(valeurs):
    modules_restants = []
    for module in INDEX_MODULES:
        idx_n, idx_c = INDEX_MODULES[module]
        if str(valeurs[idx_n]) == "" :
            modules_restants.append(module)
    return modules_restants