nMax = 4
v1, v2 = [], []
n = 0
value = 0
result = 0


while not (n in range(1,nMax + 1)):
	n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ?  "))



print("Saisie du premier vecteur : ", end="\n")
for k2 in range(0,n):
	value = int(input(f"v1[{k2}] = "))
	v1.append(value)
print("Saisie du second vecteur : ", end="\n")
for k2 in range(0,n):
	value = int(input(f"v2[{k2}] = "))
	v2.append(value)

for p in range(0,n):
	result += (v1[p] * v2[p])


print("Le produit scalaire de v1 par v2 vaut", result)


