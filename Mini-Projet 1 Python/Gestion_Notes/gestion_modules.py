COEFFICIENTS = {}

LISTE_MODULES = ["Algèbre 1","Analyse 1","MTU","P. Python","Algorithmique et p. C","Architecture fonctionnement des ordinateurs","Électronique numérique"]

def ajouter_coefficient(module, coefficient):
    COEFFICIENTS[module] = coefficient

def get_coefficients():
    return COEFFICIENTS

def est_complet():
    return len(COEFFICIENTS) >= 7

def get_modules_restants():
    restants = []
    for m in LISTE_MODULES:
        if m not in COEFFICIENTS:
            restants.append(m)
    return restants