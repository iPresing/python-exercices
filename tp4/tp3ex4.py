import random

Range = 0
while Range <= 0:
        Range = int(input("Jusqu'à quelle valeur la liste peut s'étendre ? : "))
#L1 = [2, 8, 5, 6, 8, 3, 3, 3, 3, 8, 6]
L1 = [random.randint(1, Range) for _ in range(11)]
Max = 1
Max_occur = 1
u = -1

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.

** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
L1.sort(reverse=True)
print(L1)

for n in L1:
	u += 1
	if L1.count(n) == Max_occur:
		if L1[u] > Max:
			Max = L1[u]
	elif Max_occur < L1.count(n):
		Max = L1[u]
		Max_occur = L1.count(n)
	else:
		print(".")
print("le nombre le plus frequent dans la liste est le : {} ({} x)".format(Max, Max_occur))

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
