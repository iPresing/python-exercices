# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []
NotesInd = float(0)
sum = 0
#  -------> universData = range(0,21) (plus utile)

#ecart = []

for p in range(0,nombreEtudiants):
    NotesInd = float(input(f" Note etudiant {p} : "))
    while not isinstance(NotesInd, range(0, 21)):

        print("Veuillez saisir une note entre 0 et 20")
        NotesInd = float(input(f" Note etudiant {p} : "))

    # -------> sum += NotesInd (obselète)
    notes.append(NotesInd)
    #print(f"Note etudiant {p} : {notes[p]}")
    #NotesInd = float(input(f" Note etudiant {p} :"))
    #ecart.append((p,NotesInd))

moyenne = sum(notes) / nombreEtudiants

print(f"\nMoyenne de classe : {round(moyenne,1)}")
print("\nNuméro de l’Etudiant | note | ecart a la moyenne", end="\n")
for n in range(0, nombreEtudiants):
    ecart = ((moyenne - int(notes[n])))
    ecart = round(ecart, 2)
    #if ecart < 0:
        #ecart = -ecart

    print(n,notes[n],ecart,sep= " | ", end="\n")
    #print(f"{n,notes[n], {moyenne - int(notes[n])}", sep=" | ", end="\n")




