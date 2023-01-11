caca = [5, 2, 4, 8, 1, 3]

 #caca.sort() # question 3 : ceci permet de faire la même chose mais de façon plus rapide


def tri(liste, min_val=99999):
	for value in liste:
		print(liste)
		pos_max = liste.index(value)
		for pos in range((len(liste) - 1), pos_max, -1):
			if value > liste[pos]:
				if min_val > liste[pos]:
					min_val = liste[pos]
		if min_val != 99999:
			pos_max = liste.index(value)
			pos_min = liste.index(min_val)

			liste[pos_max], liste[pos_min] = min_val, value
			min_val = 99999
	#return print(f"La liste triée est : {liste}")

print(tri(caca)) # question 2 : il retourne None car aucune donné lui est retourné
print(caca) #question 2 : cependant la liste a bien été triée