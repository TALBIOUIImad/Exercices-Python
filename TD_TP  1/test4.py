note = float(input("Veuillez entrer un nombre (sur 20) : "))
while note < 0 or note > 20 :
    note = float(input("Veuillez entrer un nombre (sur 20) : "))
while note > 0 and note <= 20 :
    if note < 10 :
        print("Non valide")
        break
    elif note == 10 :
        print("Admis")
        break
    elif note < 14 :
        print("Assez bien")
        break
    elif note < 16 :
        print("bien")
        break
    else:
        print("tres bien")
        break