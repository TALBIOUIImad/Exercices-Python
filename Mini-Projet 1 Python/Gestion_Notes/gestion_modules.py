#les modules d'enseignement et leur coef
    #dic pour stoker les coef de chaque module
COEFFICIENTS = {}                     
    #liste des 7 modules qui d'enseignement dans S1 info.app
LISTE_MODULES = ["Algèbre 1","Analyse 1","MTU","P. Python","Algorithmique et p. C","Architecture fonctionnement des ordinateurs","Électronique numérique"]

    #ajouter le coef d'un module entre 1 et 10
def ajouter_coefficient(module, coefficient):
    COEFFICIENTS[module] = coefficient

    #retourner le dic complete des coefs   (on utilise sa pour stoker dans treeview dans l'interface,calcul total et moyenne,relve et charger les donnees.)
def get_coefficients():
    return COEFFICIENTS

    #verifier si tous les 7 modules ont un coef
def est_complet():
    return len(COEFFICIENTS) >= 7

    #retourner la liste des modules qui n'ont pas encore de coef (utiliser dans combobox des coef)
def get_modules_restants():
    restants = []
    for m in LISTE_MODULES:
        if m not in COEFFICIENTS:
            restants.append(m)
    return restants