
s1 = input("Veuillez entrer la note du module 1 et le coeff correspondant : ")
s2 = s1.split(" ")

s2 = list(map(int, s2))

coef = []
notes = []

[coef.append(int(s2[n])) for n in range(1, int(len(s2)), 2)]
[notes.append(int(s2[p]*s2[p-1])) for p in range(1, int(len(s2)), 2)]

moyenne = round((sum(notes)/sum(coef)), 1)

print(f"La moyenne est de {moyenne}") if moyenne != None else print("Aucune note ?")
print("L'élève est admis") if (moyenne >= 10) and (not range(0,9) in notes) else print("L'élève n'est pas admis")
