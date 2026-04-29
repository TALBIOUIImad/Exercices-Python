import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Calculatrice")
fenetre.geometry("318x485+1+1")
fenetre.resizable(False, False)
fenetre.config(background="#8F8E8D")

resultat = tk.Frame(height=80, width=400, background="#DBDAD9")
resultat.pack()

Bouttons = tk.Frame(height=500, width=400, background="#8F8E8D")
Bouttons.pack()

operation_txt = ""
operation = tk.StringVar()

def button_click(btn):
    global operation_txt

    if btn == "C":
        operation_txt = ""
        operation.set(operation_txt)
        return

    if btn == "=":
        try:
            operation_txt = str(eval(operation_txt))
        except Exception:
            operation_txt = "Erreur"
        operation.set(operation_txt)
        return

    if btn == "+/-":
        if operation_txt.startswith("-"):
            operation_txt = operation_txt[1:]
        else:
            operation_txt = "-" + operation_txt
        operation.set(operation_txt)
        return

    if btn == "%":
        try:
            operation_txt = str(eval(operation_txt) / 100)
        except Exception:
            operation_txt = "Erreur"
        operation.set(operation_txt)
        return

    operation_txt += str(btn)
    operation.set(operation_txt)

label_resultat = tk.Label(
    resultat,
    textvariable=operation,
    font=("Consolas", 35),
    bg="white",
    width=24,
    height=2,
)
label_resultat.pack()

# ligne 1
btn1 = tk.Button(Bouttons, text="C", height=5, width=10, bg="#A5A5A5", command=lambda: button_click("C"))
btn1.place(x=0, y=0)

btn2 = tk.Button(Bouttons, text="+/-", height=5, width=10, bg="#A5A5A5", command=lambda: button_click("+/-"))
btn2.place(x=80, y=0)

btn3 = tk.Button(Bouttons, text="%", height=5, width=10, bg="#A5A5A5", command=lambda: button_click("%"))
btn3.place(x=160, y=0)

btn4 = tk.Button(Bouttons, text="/", height=5, width=10, bg="#FF9500", fg="white", command=lambda: button_click("/"))
btn4.place(x=240, y=0)

# ligne 2
btn5 = tk.Button(Bouttons, text="7", height=5, width=10, fg="white", bg="#505050", command=lambda: button_click("7"))
btn5.place(x=0, y=80)

btn6 = tk.Button(Bouttons, text="8", height=5, width=10, fg="white", bg="#505050", command=lambda: button_click("8"))
btn6.place(x=80, y=80)

btn7 = tk.Button(Bouttons, text="9", height=5, width=10, fg="white", bg="#505050", command=lambda: button_click("9"))
btn7.place(x=160, y=80)

btn8 = tk.Button(Bouttons, text="*", height=5, width=10, bg="#FF9500", fg="white", command=lambda: button_click("*"))
btn8.place(x=240, y=80)

# ligne 3
btn9 = tk.Button(Bouttons, text="4", height=5, width=10, fg="white", bg="#505050", command=lambda: button_click("4"))
btn9.place(x=0, y=160)

btn10 = tk.Button(Bouttons, text="5", height=5, width=10, fg="white", bg="#505050", command=lambda: button_click("5"))
btn10.place(x=80, y=160)

btn11 = tk.Button(Bouttons, text="6", height=5, width=10, fg="white", bg="#505050", command=lambda: button_click("6"))
btn11.place(x=160, y=160)

btn12 = tk.Button(Bouttons, text="-", height=5, width=10, bg="#FF9500", fg="white", command=lambda: button_click("-"))
btn12.place(x=240, y=160)

# ligne 4
btn13 = tk.Button(Bouttons, text="1", height=5, width=10, fg="white", bg="#505050", command=lambda: button_click("1"))
btn13.place(x=0, y=240)

btn14 = tk.Button(Bouttons, text="2", height=5, width=10, fg="white", bg="#505050", command=lambda: button_click("2"))
btn14.place(x=80, y=240)

btn15 = tk.Button(Bouttons, text="3", height=5, width=10, fg="white", bg="#505050", command=lambda: button_click("3"))
btn15.place(x=160, y=240)

btn16 = tk.Button(Bouttons, text="+", height=5, width=10, bg="#FF9500", fg="white", command=lambda: button_click("+"))
btn16.place(x=240, y=240)

# ligne 5
btn17 = tk.Button(Bouttons, text="0", height=5, width=22, fg="white", bg="#505050", command=lambda: button_click("0"))
btn17.place(x=0, y=320)

btn18 = tk.Button(Bouttons, text=".", height=5, width=10, fg="white", bg="#505050", command=lambda: button_click("."))
btn18.place(x=160, y=320)

btn19 = tk.Button(Bouttons, text="=", height=5, width=10, bg="#FF9500", fg="white", command=lambda: button_click("="))
btn19.place(x=240, y=320)

fenetre.mainloop()