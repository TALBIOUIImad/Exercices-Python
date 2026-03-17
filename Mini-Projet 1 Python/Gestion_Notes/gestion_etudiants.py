ETUDIANTS = []
ID_auto = 1

def valider_nom_prenom(txt):
    if txt == "":
        return True
    if txt[0] == " ":
        return False
    if txt.count(" ") > 2:
        return False
    if "   " in txt:
        return False
    caracteres = " -_éèêëàâáäúčñùûîïôç"
    for char in txt:
        if char.isalpha():
            continue
        elif char in caracteres:
            continue
        else:
            return False
    return True

def valider_cne(txt):
    if txt == "":
        return True
    if " " in txt:
        return False
    for char in txt:
        if char.isalpha() or char.isdigit():
            continue
        else:
            return False
    return True

def ajouter_etudiant(nom, prenom, cne):
    global ID_auto
    for e in ETUDIANTS:
        if e["cne"] == cne:
            return None
    etudiant = {"Id": ID_auto, "Nom": nom, "Prenom": prenom, "cne": cne}
    ETUDIANTS.append(etudiant)
    ID_auto += 1
    return etudiant

def supprimer_etudiant(id_supp):
    for etudiant in ETUDIANTS:
        if str(etudiant["Id"]) == str(id_supp):
            ETUDIANTS.remove(etudiant)
            break

def modifier_etudiant(id_mod, nom, prenom, cne):
    for etudiant in ETUDIANTS:
        if str(etudiant["Id"]) == str(id_mod):
            etudiant["Nom"] = nom
            etudiant["Prenom"] = prenom
            etudiant["cne"] = cne
            break

def get_etudiants():
    return ETUDIANTS

def get_noms_complets():
    liste = []
    for e in ETUDIANTS:
        liste.append(e["Nom"] + " " + e["Prenom"])
    return liste