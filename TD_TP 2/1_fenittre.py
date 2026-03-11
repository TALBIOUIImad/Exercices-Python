#==> p1
import tkinter as tk
#from tkinter import messagebox
fenetre = tk.Tk()
fenetre.title("Application")
fenetre.geometry("400x300")
#p2
#label = tk.Label(fenetre,text="Bonjour")
#label.pack()
#def dire_bonjour():
#    print("Cv !")
#btn = tk.Button(fenetre, text="Cliquer ici",command=dire_bonjour)
#btn.pack()
#p3
#entree = tk.Entry(fenetre)
#entree.pack()
#def affichier_nom():
#    nom = entree.get()
#    label.config(text="Bnjour " + nom)
#bouton = tk.Button(fenetre,text="valider",command=affichier_nom)
#bouton.pack()
#p4
tk.Label(fenetre,text="Entrer votre nom : ").grid(row=0, column=0)
entree_nom = tk.Entry(fenetre)
entree_nom.grid(row=0,column=1)
tk.Label(fenetre,text="Entrer votre prenom : ").grid(row=1, column=0)
entree_prenom = tk.Entry(fenetre)
entree_prenom.grid(row=1,column=1)
label = tk.Label(fenetre, text="")
label.grid(row=3,column=1)
def affichier_nom():
    nom = entree_nom.get()
    prenom = entree_prenom.get()
    label.config(text="Bonjour " + nom + " " + prenom)
bouton = tk.Button(fenetre,text="valider",command=affichier_nom)
bouton.grid(row=2,column=1)
#p5
#messagebox.showinfo("Information", "Operation terminee")
fenetre.mainloop()