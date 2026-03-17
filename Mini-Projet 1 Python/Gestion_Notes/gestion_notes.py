INDEX_MODULES = {"Algèbre 1": (4, 5),"Analyse 1": (6, 7),"MTU": (8, 9),"P. Python": (10, 11),"Algorithmique et p. C": (12, 13),"Architecture fonctionnement des ordinateurs": (14, 15),"Électronique numérique": (16, 17)}

def get_index(module):
    return INDEX_MODULES[module]

def get_all_index():
    return INDEX_MODULES

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

def calculer_total_moyenne(valeurs):
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
    for module in INDEX_MODULES:
        idx_n, idx_c = INDEX_MODULES[module]
        Total += float(valeurs[idx_n]) * int(valeurs[idx_c])
        Total_coef += int(valeurs[idx_c])
    Moyenne = float(format(Total / Total_coef,".2f"))
    Total = float(format(Total,".2f"))
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

def get_modules_restants_etudiant(valeurs):
    modules_restants = []
    for module in INDEX_MODULES:
        idx_n, idx_c = INDEX_MODULES[module]
        if str(valeurs[idx_n]) == "" or str(valeurs[idx_n]) == "0":
            modules_restants.append(module)
    return modules_restants