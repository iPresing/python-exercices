# exercice1 #

x = int(input("Entrez x:"))
y = int(input("Entrez y:"))
temp = 0


print("Avant permutation :",f" x : {x}",f" y : {y}", sep="\n")

temp = x
x = y
y = temp

print("Apres permutation :",f" x : {x}",f" y : {y}", sep="\n")

###############
