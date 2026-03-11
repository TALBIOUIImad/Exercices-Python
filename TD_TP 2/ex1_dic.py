users = {"admin" : "1234","imad TLBR" : "700856","abdsamad" : "joj22"}
def login(username,mdp):
    if username not in users :
        print("Username inexistant")
    elif users[username] != mdp :
        print("Mot de pass errone")
    else :
        print("Connexion reussie")
username = input("Veuillez entrer username : ")
mdp = input("Veuillez entrer votre mot de passe : ")
login(username,mdp)