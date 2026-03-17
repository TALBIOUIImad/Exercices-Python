
ETUDIANTS = []       #Ce Liste Qui stocker tous les etudiants sous forme d'un dictionnaire {Id,nom,prenom,cne}
ID_auto = 1               #compeur auto croissante pour id unique de chaque etudiants 

# fcts de validation des entrees
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

#  fcts des (ajoute,modifier,supprimer)

def ajouter_etudiant(nom, prenom, cne):
    global ID_auto
    for e in ETUDIANTS:                # verifier de l'unicite du CNE
        if e["cne"] == cne:  
            return None
    etudiant = {"Id": ID_auto, "Nom": nom, "Prenom": prenom, "cne": cne}
    ETUDIANTS.append(etudiant)
    ID_auto += 1
    return etudiant

   #update de compteur d'id_auto (utiliser dans le charger des donnees pour commencer la numeration) 
def set_id_auto(new_id):
    global ID_auto
    ID_auto = new_id
    
def supprimer_etudiant(id_supp):
    for etudiant in ETUDIANTS:            #supp l'etudiant Par son id 
        if str(etudiant["Id"]) == str(id_supp):
            ETUDIANTS.remove(etudiant)
            break

def modifier_etudiant(id_mod, nom, prenom, cne):
    for etudiant in ETUDIANTS:                               
        if str(etudiant["Id"]) == str(id_mod):     #recherche l'etudiant par id avant mod (nom,prenom,cne)
            etudiant["Nom"] = nom
            etudiant["Prenom"] = prenom
            etudiant["cne"] = cne
            break
# fcts de lecture des donnees
    #retourner la listecomplete des etudiants(nom,prenom,cne) ->(interface)
def get_etudiants():
    return ETUDIANTS

    #retourner la listecomplete des etudiants(nom,prenom) ->(combobox --> note)
def get_noms_complets():
    liste = []
    for e in ETUDIANTS:
        liste.append(e["Nom"] + " " + e["Prenom"])
    return liste