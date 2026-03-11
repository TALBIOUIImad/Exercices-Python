note = []
for i in range(9) :
    n = input(f"Entre l'elemente {i+1} : ")
    note.append(n)
print(note)
note.insert(6,'tlb')
print(note)
print(len(note))
note.remove('1')
print(note)
note.pop(6)
print(note)
note.clear()
print(note)