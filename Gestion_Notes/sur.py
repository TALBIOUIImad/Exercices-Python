import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from gestion_etudiants import *
from gestion_modules import *
from gestion_notes import *
from fichier import sauvegarder_excel, charger_excel

liste_nom_complet = []

fenetre = tk.Tk()
fenetre.title("Application de Gestion de Notes.")
fenetre.geometry("1690x780+1+1")
fenetre.configure(background="#E5E4E2")

Title = tk.Label(fenetre, text="Gestion de Notes", bg="dark blue",
                 font=("monospace", 17, "bold"), fg="white")
Title.pack(fill="x")

part_frame = tk.Frame(fenetre, bg="white", width=300, height=400)
part_frame.pack(side="left", fill="y")
part_frame.pack_propagate(False)

# ========= VERIFICATION =========
def verifier_av():
    if len(get_etudiants()) > 0 and est_complet():
        bouton_note.config(state="normal")
    else:
        bouton_note.config(state="disabled")

# ========= ÉTUDIANTS =========
vcmd_nom = fenetre.register(valider_nom_prenom)
vcmd_cne_v = fenetre.register(valider_cne)

def Boutton_ajoute():
    NOM = Entrer_nom.get().strip()
    PRENOM = Entrer_prenom.get().strip()
    CNE = Entrer_cne.get().strip()
    if NOM == "" or PRENOM == "" or CNE == "":
        messagebox.showinfo("Erreur", "Remplir les cas.")
        return
    etudiant = ajouter_etudiant(NOM, PRENOM, CNE)
    if etudiant is None:
        messagebox.showinfo("Erreur", "CNE déjà existant!")
        return
    donnee_table.insert("", "end", values=(
        etudiant["Id"], etudiant["Nom"],
        etudiant["Prenom"], etudiant["cne"],
        "", "", "", "", "", "", "", "", "", "",
        "", "", "", "", 0, 0, ""
    ))
    liste_nom_complet.clear()
    liste_nom_complet.extend(get_noms_complets())
    combo_box_etd["values"] = liste_nom_complet
    Entrer_nom.delete(0, tk.END)
    Entrer_prenom.delete(0, tk.END)
    Entrer_cne.delete(0, tk.END)
    verifier_av()

def Boutton_supprimer():
    selection = donnee_table.selection()
    if not selection:
        return
    values = donnee_table.item(selection)["values"]
    id_supp = values[0]
    supprimer_etudiant(id_supp)
    donnee_table.delete(selection)
    liste_nom_complet.clear()
    liste_nom_complet.extend(get_noms_complets())
    combo_box_etd["values"] = liste_nom_complet
    combo_box_etd.set("")
    verifier_av()

def Boutton_modifier():
    selection = donnee_table.selection()
    if not selection:
        return
    values = donnee_table.item(selection)["values"]
    id_mod = values[0]
    nom = Entrer_nom.get().strip()
    prenom = Entrer_prenom.get().strip()
    CNE = Entrer_cne.get().strip()
    if nom == "" or prenom == "" or CNE == "":
        messagebox.showinfo("Erreur", "Remplir les cas.")
        return
    modifier_etudiant(id_mod, nom, prenom, CNE)
    donnee_table.item(selection, values=(id_mod, nom, prenom, CNE))
    liste_nom_complet.clear()
    liste_nom_complet.extend(get_noms_complets())
    combo_box_etd["values"] = liste_nom_complet
    combo_box_etd.set("")
    Entrer_nom.delete(0, tk.END)
    Entrer_prenom.delete(0, tk.END)
    Entrer_cne.delete(0, tk.END)

# ========= WIDGETS ÉTUDIANTS =========
LBL_titre_etd = tk.Label(part_frame, text="Étudiants :", bg="white",
                          font=("helvetica", 10, "bold"))
LBL_titre_etd.place(x=1, y=1)
LBL_nom = tk.Label(part_frame, text="Nom :", bg="white")
LBL_nom.place(x=55, y=20)
Entrer_nom = tk.Entry(part_frame, bd="2", justify="center",
                       validate="key", validatecommand=(vcmd_nom, "%P"))
Entrer_nom.place(x=95, y=20)
LBL_prenom = tk.Label(part_frame, text="Prenom :", bg="white")
LBL_prenom.place(x=40, y=45)
Entrer_prenom = tk.Entry(part_frame, bd="2", justify="center",
                          validate="key", validatecommand=(vcmd_nom, "%P"))
Entrer_prenom.place(x=95, y=45)
LBL_cne = tk.Label(part_frame, text="CNE :", bg="white")
LBL_cne.place(x=59, y=70)
Entrer_cne = tk.Entry(part_frame, bd="2", justify="center",
                       validate="key", validatecommand=(vcmd_cne_v, "%P"))
Entrer_cne.place(x=95, y=70)
btn_ajoute = tk.Button(part_frame, text="Ajouter", bg="#3EB489",
                        command=Boutton_ajoute)
btn_ajoute.place(x=125, y=95)
LBL_selec = tk.Label(part_frame, text="Sélectionner :", bg="white")
LBL_selec.place(x=1, y=126)
btn_supp = tk.Button(part_frame, text="Supprimer", bg="#CF1020",
                      command=Boutton_supprimer)
btn_supp.place(x=80, y=125)
btn_mod = tk.Button(part_frame, text="Modifier", bg="#0FC0FC",
                     command=Boutton_modifier)
btn_mod.place(x=152, y=125)
canvas_1 = tk.Canvas(part_frame, height=2)
canvas_1.place(x=1, y=155)
canvas_1.create_line(0, 1, 400, 1)

# ========= TABLEAU =========
colonnes = ("Id", "Nom", "Prenom", "CNE",
            "Algèbre 1", "Coeff_Alg", "Analyse 1", "Coeff_Ana",
            "MTU", "Coeff_MTU", "P. Python", "Coeff_Py",
            "Algo et p. C", "Coeff_Algo", "Archi des ordinateurs", "Coeff_Arc",
            "Électronique num", "Coeff_E_N",
            "Total", "Moyenne", "Mention")
donnees_frame = tk.Frame(fenetre, bg="#F5F5F5", width=1250, height=600)
donnees_frame.pack(side="left", fill="both", expand=True)
scroll_donnees_x = tk.Scrollbar(donnees_frame, orient=tk.HORIZONTAL)
scroll_donnees_y = tk.Scrollbar(donnees_frame, orient=tk.VERTICAL)
donnee_table = ttk.Treeview(donnees_frame, columns=colonnes, show="headings",
                             height=10, xscrollcommand=scroll_donnees_x.set,
                             yscrollcommand=scroll_donnees_y.set)
scroll_donnees_x.pack(side="bottom", fill="x")
scroll_donnees_y.pack(side="right", fill="y")
donnee_table.pack(fill="both", expand=True)
scroll_donnees_x.config(command=donnee_table.xview)
scroll_donnees_y.config(command=donnee_table.yview)

for col in colonnes:
    donnee_table.heading(col, text=col)
    donnee_table.column(col, width=80, anchor="center")

# ========= COEFFICIENTS =========
LBL_Coeff_mdl = tk.Label(part_frame, text="Coefficient de modules :", bg="white",
                          font=("helvetica", 10, "bold"))
LBL_Coeff_mdl.place(x=1, y=160)
LBL_mdl = tk.Label(part_frame, text="Les modules :", bg="white")
LBL_mdl.place(x=120, y=190)
combo_box = ttk.Combobox(part_frame, values=LISTE_MODULES,
                          state="readonly", width=35)
combo_box.set(LISTE_MODULES[0])
combo_box.place(x=40, y=210)
LBL_coeff = tk.Label(part_frame, text="Coefficient :", bg="white")
LBL_coeff.place(x=120, y=240)
spinbox = tk.Spinbox(part_frame, from_=1, to=10, bd=2)
spinbox.place(x=80, y=260)
table_coeff = ttk.Treeview(part_frame, columns=("Module", "Coefficient"),
                            show="headings", height=7)
table_coeff.heading("Module", text="Module")
table_coeff.heading("Coefficient", text="Coefficient")
table_coeff.column("Module", width=100)
table_coeff.column("Coefficient", width=100, anchor="center")
table_coeff.place(x=40, y=295)

def ajouter_Coeff():
    if est_complet():
        messagebox.showinfo("Info", "Tous les coefficients sont entrés.")
        return
    module = combo_box.get()
    coefficient = int(spinbox.get())
    ajouter_coefficient(module, coefficient)
    table_coeff.insert("", "end", values=(module, coefficient))
    restants = get_modules_restants()
    combo_box["values"] = restants
    if restants:
        combo_box.set(restants[0])
    else:
        combo_box.set("")
    verifier_av()

bouton_coff = tk.Button(part_frame, text="Sauvegarder", bg="#3EB489",
                         command=ajouter_Coeff)
bouton_coff.place(x=100, y=461)
canvas_2 = tk.Canvas(part_frame, height=2)
canvas_2.place(x=1, y=498)
canvas_2.create_line(0, 1, 400, 1)

# ========= NOTES =========
verf = fenetre.register(valider_note)

def stocker_notes():
    try:
        etudiant_nom = combo_box_etd.get()
        module = combo_box_note.get()
        note = Entrer_note.get()
        if etudiant_nom == "" or module == "" or note == "":
            messagebox.showinfo("Erreur", "Remplir tous les champs")
            return
        coefficients = get_coefficients()
        coef = coefficients[module]
        note = float(note)
        etudiants = get_etudiants()
        etudiant = None
        for e in etudiants:
            if e["Nom"] + " " + e["Prenom"] == etudiant_nom:
                etudiant = e
                break
        index = get_all_index()
        for item in donnee_table.get_children():
            valeurs = list(donnee_table.item(item)["values"])
            if str(valeurs[0]) == str(etudiant["Id"]):
                idx_n, idx_c = index[module]
                valeurs[idx_n] = note
                valeurs[idx_c] = coef
                donnee_table.item(item, values=valeurs)
                
                resultat = calculer_total_moyenne(valeurs, coefficients)
                if resultat:
                    valeurs[18] = resultat["total"]
                    valeurs[19] = resultat["moyenne"]
                    valeurs[20] = resultat["mention"]
                    donnee_table.item(item, values=valeurs)
                break
        current_values = list(combo_box_note["values"])
        if module in current_values:
            current_values.remove(module)
            combo_box_note["values"] = current_values
        if current_values:
            combo_box_note.set(current_values[0])
        else:
            combo_box_note.set("")
        Entrer_note.delete(0, tk.END)
    except Exception as err:
        print("ERREUR:", err)

LBL_note_mdl = tk.Label(part_frame, text="Note du module :", bg="white",
                          font=("helvetica", 10, "bold"))
LBL_note_mdl.place(x=1, y=505)
LBL_choi_etd = tk.Label(part_frame, text="Étudiants :", bg="white")
LBL_choi_etd.place(x=15, y=535)
combo_box_etd = ttk.Combobox(part_frame, state="readonly", width=30)
combo_box_etd.place(x=75, y=535)
LBL_choi_mdl = tk.Label(part_frame, text="Les modules :", bg="white")
LBL_choi_mdl.place(x=1, y=565)
combo_box_note = ttk.Combobox(part_frame, values=LISTE_MODULES,
                               state="readonly", width=30)
combo_box_note.set(LISTE_MODULES[0])
combo_box_note.place(x=78, y=565)
LBL_ent_note = tk.Label(part_frame, text="Note :", bg="white")
LBL_ent_note.place(x=100, y=600)
Entrer_note = tk.Entry(part_frame, bd="2", justify="center", width=8,
                        validate="key", validatecommand=(verf, "%P"))
Entrer_note.place(x=140, y=600)
bouton_note = tk.Button(part_frame, text="Sauvegarder", bg="#3EB489",
                         command=stocker_notes, state="disabled")
bouton_note.place(x=127, y=640)

# ========= SAUVEGARDER / CHARGER =========
canvas_3 = tk.Canvas(part_frame, height=2)
canvas_3.place(x=1, y=670)
canvas_3.create_line(0, 1, 400, 1)

def btn_sauvegarder():
    try:
        sauvegarder_excel(donnee_table, get_coefficients())
        messagebox.showinfo("Succès", "Données sauvegardées!")
    except Exception as err:
        messagebox.showinfo("Erreur", str(err))

def btn_charger():
    try:
        fichier = filedialog.askopenfilename(
            title="Choisir un fichier",
            filetypes=[("Excel", "*.xlsx")]
        )
        if fichier == "":
            return
        etudiants_data, coefficients_data, lignes = charger_excel(fichier)
        for item in donnee_table.get_children():
            donnee_table.delete(item)
        ETUDIANTS.clear()
        ETUDIANTS.extend(etudiants_data)
        COEFFICIENTS.clear()
        COEFFICIENTS.update(coefficients_data)
        for ligne in lignes:
            donnee_table.insert("", "end", values=ligne)
        liste_nom_complet.clear()
        liste_nom_complet.extend(get_noms_complets())
        combo_box_etd["values"] = liste_nom_complet
        for item in table_coeff.get_children():
            table_coeff.delete(item)
        for module, coef in coefficients_data.items():
            table_coeff.insert("", "end", values=(module, coef))
        messagebox.showinfo("Succès", "Données chargées!")
    except Exception as err:
        messagebox.showinfo("Erreur", str(err))

btn_save = tk.Button(part_frame, text="💾 Sauvegarder", bg="#1976d2",
                      fg="white", command=btn_sauvegarder)
btn_save.place(x=30, y=680)
btn_load = tk.Button(part_frame, text="📂 Charger", bg="#1976d2",
                      fg="white", command=btn_charger)
btn_load.place(x=160, y=680)

fenetre.mainloop()