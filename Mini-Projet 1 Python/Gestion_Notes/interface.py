#interface graphique
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
#import les  modules de gestion
from gestion_etudiants import *
from gestion_modules import *
from gestion_notes import *
from fichier_excel import *
# save dans le meme dossier
dossier = os.path.dirname(os.path.abspath(__file__))
NOTES_MODULES = {}
notes = []
#verification de condions pour activer ou desactiver le botton (note,sauvgarder dans excel) 
def verifier_av():
    if len(get_etudiants()) > 0 and est_complet() :
        bouton_note.config(state="normal")
    else:
        bouton_note.config(state="disabled")
    if len(get_etudiants()) > 0 :
        btn_save.config(state="normal")
    else:
        btn_save.config(state="disabled")
    
#Configuration de la fenetre principale
fenetre = tk.Tk()
fenetre.title("Application de Gestion de Notes.")
fenetre.state("zoomed")
fenetre.configure(background="#E5E4E2")
#titre de l'app
Title = tk.Label(fenetre,text="Gestion de Notes",bg="dark blue",font=("monospace",17,"bold"),fg="white")
Title.pack(fill="x")
#frame menu (gauche)
part_frame = tk.Frame(fenetre,bg="white",width=300,height=400)
part_frame.pack(side="left",fill="y")
part_frame.pack_propagate(False)
# Section 1 : Gestion des etudiants
    #validation pour les entry
vcmd_nom_prenom = fenetre.register(valider_nom_prenom)
vcmd_cne = fenetre.register(valider_cne)
def Boutton_ajoute():
    NOM = Entrer_nom.get().strip()
    PRENOM = Entrer_prenom.get().strip()
    CNE = Entrer_cne.get().strip()
    #si les champs sont vides
    if NOM == "" or PRENOM == "" or CNE == "" :
        messagebox.showinfo("Erreur","Remplir les cas.")
        return
    #l'appel de fct
    etudiant = ajouter_etudiant(NOM,PRENOM,CNE)
    #si none le cne est deja existe
    if etudiant is None :
        messagebox.showinfo("Erreur","CNE deja existant!")
        return
    #inserer dans le tableau avec 21 colonnes (notes et coefs est vides)
    donnee_table.insert("","end",values=(etudiant["Id"],etudiant["Nom"],etudiant["Prenom"],etudiant["cne"],"","","","","","","","","","","","","","",0,0,""))
    # mise a jour des entry
    combo_box_etd["values"] = get_noms_complets()
    Entrer_nom.delete(0,tk.END)
    Entrer_prenom.delete(0,tk.END)
    Entrer_cne.delete(0,tk.END)
    #verifier les condition d'activation
    verifier_av()
def Boutton_supprimer():
    #recuperer l'id de l'etudiant selectionne
    selection = donnee_table.selection()
    if not selection:
        return
    values = donnee_table.item(selection)["values"]
    id_supp = values[0]
    #supp de liste ETUDIANTS
    supprimer_etudiant(id_supp)
    #supp du tableau
    donnee_table.delete(selection)
    #mise a jour la combobox de note 
    combo_box_etd["values"] = get_noms_complets()
    combo_box_etd.set("")
    
def Boutton_modifier():
    selection = donnee_table.selection()
    if not selection:
        messagebox.showinfo("Erreur","Selectionner un etudiant!")
        return
    NOM = Entrer_nom.get().strip()
    PRENOM = Entrer_prenom.get().strip()
    CNE = Entrer_cne.get().strip()
    if NOM == "" or PRENOM == "" or CNE == "" :
        messagebox.showinfo("Erreur","Remplir les cas.")
        return
    #recuperer l'id de l'etudiant selectionne
    values = donnee_table.item(selection)["values"]
    id_mod = values[0]
    #modifier dans la liste ETUDIANTS
    modifier_etudiant(id_mod,NOM,PRENOM,CNE)
    #garder les anciennes valeurs des notes et modifier unuquement (nom,prenom,cne)
    old_values = list(donnee_table.item(selection)["values"])
    old_values[1] = NOM
    old_values[2] = PRENOM
    old_values[3] = CNE
    donnee_table.item(selection,values=old_values)
    #mis a jour de conbobox de note
    combo_box_etd["values"] = get_noms_complets()
    combo_box_etd.set("")
    # mise a jour des entry
    Entrer_nom.delete(0,tk.END)
    Entrer_prenom.delete(0,tk.END)
    Entrer_cne.delete(0,tk.END)
#menu dans section info Etudiants
    #titre de la section
LBL_nom = tk.Label(part_frame,text="Etudians :",bg="white",font=("helvetica",10,"bold"))
LBL_nom.place(x=1,y=1)
    #champ Nom avec validation
LBL_nom = tk.Label(part_frame,text="Nom :",bg="white")
LBL_nom.place(x=55,y=20)
Entrer_nom = tk.Entry(part_frame,bd="2",justify="center",validate="key",validatecommand=(vcmd_nom_prenom,"%P"))
Entrer_nom.place(x=95,y=20)
    #champ Prenom avec validation
LBL_prenom = tk.Label(part_frame,text="Prenom :",bg="white")
LBL_prenom.place(x=40,y=45)
Entrer_prenom = tk.Entry(part_frame,bd="2",justify="center",validate="key",validatecommand=(vcmd_nom_prenom,"%P"))
Entrer_prenom.place(x=95,y=45)
    #champ CNE avec validation
LBL_cne = tk.Label(part_frame,text="CNE :",bg="white")
LBL_cne.place(x=59,y=70)
Entrer_cne = tk.Entry(part_frame,bd="2",justify="center",validate="key",validatecommand=(vcmd_cne,"%P"))
Entrer_cne.place(x=95,y=70)
#Label et botton des ajoute et supp et modifier
    #boutton ajouter 
btn_ajoute = tk.Button(part_frame,text="Ajouter",bg="#3EB489",command=Boutton_ajoute)
btn_ajoute.place(x=125,y=95)
LBL_selec = tk.Label(part_frame,text="Selectioner :",bg="white")
LBL_selec.place(x=1,y=126)
    #boutton supprimer
btn_supp = tk.Button(part_frame,text="Supprimer",bg="#CF1020",command=Boutton_supprimer)
btn_supp.place(x=80,y=125)
    #boutton modifier
btn_mod = tk.Button(part_frame,text="Modifier",bg="#0FC0FC",command=Boutton_modifier)
btn_mod.place(x=152,y=125)
    #ligne de separation entre les sections
canvas_1 = tk.Canvas(part_frame,height=2)
canvas_1.place(x=1,y=155)
canvas_1.create_line(0,1,400,1)
#Section 2 : tableau principal (base de donnees)
    #definition des colonnes du tableau
colonnes = ("Id","Nom","Prenom","CNE","Algèbre 1","Coeff_Alg","Analyse 1","Coeff_Ana","MTU","Coeff_MTU","P. Python","Coeff_Py","Algo et p. C","Coeff_Algo","Archi des ordinateurs","Coeff_Arc","Électronique num","Coeff_E_N","Total","Moyenne","Montion")
    #fram contenant le tableau et les scrollbars
donnees_frame = tk.Frame(fenetre,bg="#F5F5F5",width=1250,height=600)
donnees_frame.pack(side="left",fill="both",expand=True)
    #scrollbars horizontale et vertical
scroll_donnees_x = tk.Scrollbar(donnees_frame,orient=tk.HORIZONTAL)
scroll_donnees_y = tk.Scrollbar(donnees_frame,orient=tk.VERTICAL)
    #creation du treeview (tableau)
donnee_table = ttk.Treeview(donnees_frame,columns= colonnes,show="headings",height=10,xscrollcommand=scroll_donnees_x.set,yscrollcommand=scroll_donnees_y.set)
    #placement des scrollbares et tableau
scroll_donnees_x.pack(side="bottom",fill="x")
scroll_donnees_y.pack(side="right",fill="y")
donnee_table.pack(fill="both",expand=True)
scroll_donnees_x.config(command=donnee_table.xview)
scroll_donnees_y.config(command=donnee_table.yview)
    #configuration des en-tetes des colonnes
donnee_table.heading("Id",text="ID")
donnee_table.heading("Nom",text="Nom")
donnee_table.heading("Prenom",text="Prenom")
donnee_table.heading("CNE",text="CNE")
donnee_table.heading("Algèbre 1",text="Algèbre 1")
donnee_table.heading("Coeff_Alg",text="Coeff_Alg")
donnee_table.heading("Analyse 1",text="Analyse 1")
donnee_table.heading("Coeff_Ana",text="Coeff_Ana")
donnee_table.heading("MTU",text="MTU")
donnee_table.heading("Coeff_MTU",text="Coeff_MTU")
donnee_table.heading("P. Python",text="P. Python")
donnee_table.heading("Coeff_Py",text="Coeff_Py")
donnee_table.heading("Algo et p. C",text="Algo et p. C")
donnee_table.heading("Coeff_Algo",text="Coeff_Algo")
donnee_table.heading("Archi des ordinateurs",text="Archi des ordinateurs")
donnee_table.heading("Coeff_Arc",text="Coeff_Arc")
donnee_table.heading("Électronique num",text="Électronique num")
donnee_table.heading("Coeff_E_N",text="Coeff_E_N")
donnee_table.heading("Total",text="Total")
donnee_table.heading("Moyenne",text="Moyenne")
donnee_table.heading("Montion",text="Montion")
    #largeur et alignement de chaque colonne
donnee_table.column("Id",width=30,anchor="center")
donnee_table.column("Nom",width=50,anchor="center")
donnee_table.column("Prenom",width=60,anchor="center")
donnee_table.column("CNE",width=70,anchor="center")
donnee_table.column("Algèbre 1",width=70,anchor="center")
donnee_table.column("Coeff_Alg",width=80,anchor="center")
donnee_table.column("Analyse 1",width=70,anchor="center")
donnee_table.column("Coeff_Ana",width=70,anchor="center")
donnee_table.column("MTU",width=40,anchor="center")
donnee_table.column("Coeff_MTU",width=70,anchor="center")
donnee_table.column("P. Python",width=70,anchor="center")
donnee_table.column("Coeff_Py",width=70,anchor="center")
donnee_table.column("Algo et p. C",width=70,anchor="center")
donnee_table.column("Coeff_Algo",width=70,anchor="center")
donnee_table.column("Archi des ordinateurs",width=130,anchor="center")
donnee_table.column("Coeff_Arc",width=70,anchor="center")
donnee_table.column("Électronique num",width=120,anchor="center")
donnee_table.column("Coeff_E_N",width=70,anchor="center")
donnee_table.column("Total",width=70,anchor="center")
donnee_table.column("Moyenne",width=80,anchor="center")
donnee_table.column("Montion",width=80,anchor="center")
#Section 3 : gestion des coef in menu  
    #titre de sectin
LBL_Coeff_mdl = tk.Label(part_frame,text="Coefficient de modules :",bg="white",font=("helvetica",10,"bold"))
LBL_Coeff_mdl.place(x=1,y=160)
LBL_mdl = tk.Label(part_frame, text="Les modules :",bg="white")
LBL_mdl.place(x=120,y=190)
    #combobox choisir avec la liste des modules disponibles
combo_box = ttk.Combobox(part_frame,values=LISTE_MODULES,state="readonly",width=35)
combo_box.set("Algèbre 1")
combo_box.place(x=40,y=210)
LBL_coeff = tk.Label(part_frame, text="Coefficient : ",bg="white")
LBL_coeff.place(x=120,y=240)
    #spinbox pour choisir le coef (1 a 10)
spinbox = tk.Spinbox(part_frame,from_=1, to= 10,bd=2)
spinbox.place(x=80,y=260)
    #petit tableau pour affichier les coefs saisis
table_coef = ttk.Treeview(part_frame, columns=("Module", "Coefficient"), show="headings",height=7)
table_coef.heading("Module", text="Module")
table_coef.heading("Coefficient", text="Coefficient")
table_coef.column("Module", width=100)
table_coef.column("Coefficient", width=100, anchor="center")
table_coef.place(x=40,y=295)
#complet table_coef menu
def ajouter_Coeff():
    #verifier si les 7 modules sont deja configuree
    if est_complet() :
        messagebox.showinfo("Information", "Tous les Coefficients sont entrés.")
        bouton_coff.config(state="disabled")
        return
    #recuperer le module et le coef
    module = combo_box.get()
    coefficient = int(spinbox.get())
    #save dans dic COEFFICIONT
    ajouter_coefficient(module,coefficient)
    #affichier dans le petit tableau
    table_coef.insert("", "end", values=(module, coefficient))
    #retirer le module dans combobox 
    restants = get_modules_restants()
    combo_box["values"] = restants
    if restants :
        combo_box.set(restants[0])
    else:
        combo_box.set("")
    #verifier les conditions
    verifier_av()
#boutton save coef (vert)
bouton_coff = tk.Button(part_frame,text="sauvegarder",activebackground="white",bg="#3EB489",command=ajouter_Coeff)
bouton_coff.place(x=100,y=461)
#ligne de separation
canvas_2 = tk.Canvas(part_frame,height=2)
canvas_2.place(x=1,y=498)
canvas_2.create_line(0,1,400,1)


#Section 4 : saisie des notes de chaque etudiant
          #stocker la note 
def on_select_etudiant(event):
    etudiant_nom = combo_box_etd.get()
    #trouver l'etudiant dans la liste
    etudiant = None
    for e in ETUDIANTS:
        if e["Nom"] + " " + e["Prenom"] == etudiant_nom:
            etudiant = e
            break
    #trouver les modules sans note dans le treeview
    index = get_all_index()
    for item in donnee_table.get_children():
        valeurs = list(donnee_table.item(item)["values"])
        if str(valeurs[0]) == str(etudiant["Id"]):
            #recuperer les modules qui n'ont pas de note
            modules_restants = get_modules_restants_etudiant(valeurs)
            #mise a jour de combobox des modules
            combo_box_note["values"] = modules_restants
            if modules_restants:
                combo_box_note.set(modules_restants[0])
            else:
                combo_box_note.set("")
            break
def stocker_notes():
    etudiant_nom = combo_box_etd.get()
    module = combo_box_note.get()
    note = Entrer_note.get()
    #verifier si toutes les notes sont deja saisies
    if combo_box_note.get() == "" :
        messagebox.showinfo("Info", "Toutes les Notes sont saisies pour cet etudiant!")
        Entrer_note.delete(0,tk.END)
        bouton_note.config(state=tk.DISABLED)
        return
    #verifier que l'etudiant est selectionne
    if  etudiant_nom == "" :
        messagebox.showinfo("Erreur","Choisir l'etudiant!")
        return
    #verifier que saisir la note
    if note == "" :
        messagebox.showinfo("Erreur","Remplir la note!")
        return
    #recuperer le coef du module
    coef = get_coefficients()[module]
    note = float(note)
    #trouver l'etudiant dans la liste
    etudiant = None
    for e in get_etudiants() :
        if e["Nom"] + " " + e["Prenom"] == etudiant_nom:
            etudiant = e
            break
    #mise a jour de la note et coef dans le tableau
    index = get_all_index()
    for item in donnee_table.get_children():
        valeurs = list(donnee_table.item(item)["values"])
        if str(valeurs[0]) == str(etudiant["Id"]):
            #placer la note et coef dans les colonne
            idx_n, idx_c = index[module]
            valeurs[idx_n] = note
            valeurs[idx_c] = coef
            donnee_table.item(item,values=valeurs)
            #calcul total et moyenne si toutes les notes sont saisies
            resultat = calculer_total_moyenne(valeurs)
            if resultat :
                valeurs[18] = resultat["Total"]
                valeurs[19] = resultat["Moyenne"]
                valeurs[20] = resultat["Mention"]
                donnee_table.item(item,values=valeurs)
            break
    #retirer le module notee de la combobox
    current_values = list(combo_box_note["values"])
    if module in current_values:
        current_values.remove(module)
        combo_box_note["values"] = current_values
    if current_values:
        combo_box_note.set(current_values[0])
    else:
        combo_box_note.set("")
    #effacer le champ de saisie de note                  
    Entrer_note.delete(0,tk.END)
#La section des Entry notes
    #titre  de la section
LBL_note_mdl = tk.Label(part_frame,text="Note du module :",bg="white",font=("helvetica",10,"bold"))
LBL_note_mdl.place(x=1,y=505)
    #combobox de selection d'etudiant
LBL_choi_etd = tk.Label(part_frame, text="Etudiants :",bg="white")
LBL_choi_etd.place(x=15,y=535)
combo_box_etd = ttk.Combobox(part_frame,values=ETUDIANTS,state="readonly",width=30)
combo_box_etd.set("")
    #lier l'evenement de selection avec fct select_etudiant
combo_box_etd.bind("<<ComboboxSelected>>", on_select_etudiant)
combo_box_etd.place(x=75,y=535)
    #combobox de selection du modules
LBL_choi_mdl = tk.Label(part_frame, text="Les modules :",bg="white")
LBL_choi_mdl.place(x=1,y=565)
combo_box_note = ttk.Combobox(part_frame,values=LISTE_MODULES,state="readonly",width=30)
combo_box_note.set("Algèbre 1")
combo_box_note.place(x=78,y=565)
    #champ de saisie de la note avec validation (entre 0 et 20 ,deux chaiffre avant la vergule)
LBL_ent_note = tk.Label(part_frame,text="Note :",bg="white")
LBL_ent_note.place(x=100,y=600)
verf = part_frame.register(valider_note)
Entrer_note = tk.Entry(part_frame,bd="2",justify="center",width=8,validate="key",validatecommand=(verf,"%P"))
Entrer_note.place(x=140,y=600)
    #boutton save note
bouton_note = tk.Button(part_frame,text="sauvegarder",activebackground="white",bg="#3EB489",command=stocker_notes,state="disabled")
bouton_note.place(x=127,y=640)
    #ligne de separation
canvas_3 = tk.Canvas(part_frame,height=2)
canvas_3.place(x=1,y=670)
canvas_3.create_line(0,1,400,1)
#Section 5 : save et charger des donnees dans excel 
    #titre de section
LBL_excel = tk.Label(part_frame,text="Excel :",bg="white",font=("helvetica",10,"bold"))
LBL_excel.place(x=1,y=680)
    #save toutes les donnees dans un fichier Excel et affichier un mesg de succes ou d'erreur
def btn_sauvegarder():
    try:
        sauvegarder_excel(donnee_table,get_coefficients(),dossier)
        messagebox.showinfo("Succès", "Données sauvegardées!")
    except Exception as err :
        messagebox.showinfo("Erreur",str(err))
    #charger les donnees depuis un fichier excel
def btn_charger():
    try:
        #Ouvrir la boite de dialogue pour choisir le fichier
        fichier = filedialog.askopenfilename(title="Choisir un fichier",filetypes=[("Excel", "*.xlsx")])
        if fichier == "":
            return
        #charger les donnees du fichier
        etudiants_data, coef_data = charger_excel(fichier)
        #vider le tableau principal
        for item in donnee_table.get_children():
            donnee_table.delete(item)
        #vider les donnnes actuelles    
        ETUDIANTS.clear()
        COEFFICIENTS.clear()
        #vider le tableau des coefs
        for item in table_coef.get_children():
            table_coef.delete(item)
        #Remplir avec les nouvelles donnees
        ETUDIANTS.extend(etudiants_data)
        COEFFICIENTS.update(coef_data)
        #Remplir le tableau principal
        for ligne in lignes:
            donnee_table.insert("", "end", values=ligne)
        #Remplir le petit tableau des coefs
        for module, coef in coef_data.items() :
            table_coef.insert("", "end", values=(module,coef))
        #mise a jour des combobox
        combo_box_etd["values"] = get_noms_complets()
        combo_box["values"] = get_modules_restants()
        if get_modules_restants():
            combo_box.set(get_modules_restants()[0])
        else:
            combo_box.set("")
        combo_box_note["values"] = LISTE_MODULES
        combo_box_note.set("")
        #verifier les coditions
        verifier_av()
        messagebox.showinfo("Succès", "Données chargées!")
    except Exception as err :
        messagebox.showinfo("Erreur",str(err))
    #boutton save desactiver au depart
btn_save = tk.Button(part_frame, text="Sauvegarder", bg="#2e7d32",fg="white",command=btn_sauvegarder,state="disabled")
btn_save.place(x=70, y=680)
    #boutton charger
btn_charger = tk.Button(part_frame, text="Charger", bg="#1565c0",fg="white",command=btn_charger)
btn_charger.place(x=160, y=680)
#Section 6 : releve de notes
    #titre de section 
LBL_releve = tk.Label(part_frame,text="Relevé de Notes :",bg="white",font=("helvetica",10,"bold"))
LBL_releve.place(x=1,y=715)
    #Ouvrire un fenetre pour generer un releve de notes
def ouvrir_releve():
    #creer un fenetre secondaire
    top = tk.Toplevel(fenetre)
    top.title("Relevé de Notes")
    top.geometry("400x500")
    top.configure(bg="white")
    #tite
    tk.Label(top, text="Choisir un étudiant:",bg="white", font=("helvetica", 12, "bold")).pack(pady=10)
    # Liste des etudiants 
    listbox = tk.Listbox(top, width=40, height=10, font=("helvetica", 11))
    listbox.pack(pady=10)
    #trouver les etudiants qui ont toutes leurs notes
    etudiants_complets = []
    index = get_all_index()
    for e in get_etudiants() :
        for item in donnee_table.get_children():
            valeurs = list(donnee_table.item(item)["values"])
            if str(valeurs[0]) == str(e["Id"]) :
                complet = True
                for module in index :
                    #verifier chaque note
                    idx_n , idx_c = index[module]
                    note_str = str(valeurs[idx_n]).strip()
                    coef_str = str(valeurs[idx_c]).strip()
                    if note_str == "" or coef_str == "" :
                        complet = False
                        break
                    #verifier que c'est un nombre valide
                    try:
                        float(note_str)
                        float(coef_str)
                    except:
                        complet = False
                        break
                # si toutes les notes sontes completes
                if complet:
                    etudiants_complets.append(e)
                    listbox.insert("end",e["Nom"] + " " + e["Prenom"] + " - " + str(e["cne"]))
                    break
    if len(etudiants_complets) == 0 :
        messagebox.showinfo("Info","Aucun etudiant n'a toutes ses notes!")
        top.destroy()
        return
        #generer le releve de notes pour etudiant selectionne
    def btn_generer_releve():
        selection = listbox.curselection()
        if not selection:
            messagebox.showinfo("Erreur", "Choisir un étudiant!")
            return
        #recuperer l'etudiant selectionne
        index_sel = selection[0]
        etudiant = etudiants_complets[index_sel]
        #trouver ses donnees dans le tableau principal
        for item in donnee_table.get_children():
            valeurs = list(donnee_table.item(item)["values"])
            if str(valeurs[0]) == str(etudiant["Id"]):
                #generer le fichier excel
                nom_fichier = generer_releve(etudiant,valeurs,index,dossier)
                messagebox.showinfo("Succès", f"Relevé sauvegardé: {nom_fichier}")
                top.destroy()
                break
    #boutton generer releve
    btn_generer = tk.Button(top, text="Générer Relevé",bg="#1976d2", fg="white",font=("helvetica", 11, "bold"),command=btn_generer_releve)
    btn_generer.pack(pady=20)
#botton releve
btn_releve = tk.Button(part_frame, text="Relevé",bg="#e65100", fg="white",command=ouvrir_releve)
btn_releve.place(x=135, y=715)
 
 #Section 7 : chargement automatique des donnees au dernier fichier
chemin = os.path.join(dossier,"donnees_notes.xlsx")
if os.path.exists(chemin) :
    #charger les donnees du fichier excel
    etudiants_data, coef_data, lignes = charger_excel(chemin)
    #remplir les donnees des etudiants
    ETUDIANTS.extend(etudiants_data)
    #remplir les coefs
    COEFFICIENTS.update(coef_data)
    #remplir le tableau principal
    for ligne in lignes :
        donnee_table.insert("", "end", values=ligne)
    #remplir le tableau de coefs    
    for module, coef in coef_data.items() :
        table_coef.insert("", "end", values=(module,coef))
    #mise a jour combobox des etudiants
    combo_box_etd["values"] = get_noms_complets()
    #mise a jour de combobox des modules de coef
    restants = get_modules_restants()
    combo_box["values"] = restants
    if restants :
        combo_box.set(restants[0])
    else:
        combo_box.set("")
        #desactiver la boutton si tous les coefs sont saisis 
        bouton_coff.config(state=tk.DISABLED)
    #remettre la combobox des notes a la liste complete
    combo_box_note["values"] = LISTE_MODULES
    combo_box_note.set("")
    #mise a jour de compteur id_auto
    if len(get_etudiants()) > 0 :
        max_id = 0
        for e in get_etudiants() :
            if int(e["Id"]) > max_id :
                max_id = int(e["Id"])
        set_id_auto(max_id + 1)
    verifier_av()
fenetre.mainloop()