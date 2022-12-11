
HD = int(input("Donnez l’heure de début de la location (un entier) : "))
HF = int(input("Donnez l’heure de fin de la location (un entier) : "))
Univers1 = range(0,7)
Univers2 = range(7,17)
Univers3 = range(17,24)
UniversData = range(0,24)
PrixH = 0 # Prix Hors horaire
PrixA = 0 # Prix horaire
check1 = False
i = -1


def resultNcheck():

	if check1 == False:
		if HF < HD:
			print("Attention ! l'heure de la location est après la fin ...", end="\n")
			exit()
		elif HF == HD:
			print("Attention ! l’heure de fin est identique à l’heure de début.", end="\n")
			exit()
		elif not(HF in UniversData) or not(HD in UniversData):
			print("Les heures doivent être comprises entre 0 et 24 !", end="\n")
			exit()
	else:
		if PrixH == 0:
			print("Vous avez loué votre vélo pendant",
			f"{PrixA} heure(s) au tarif horaire de 1.0 euros(s)",
			f"Le montant total à payer est de {PrixA + PrixH} euro(s)", sep="\n")
		elif PrixA == 0:
			print("Vous avez loué votre vélo pendant",
			f"{PrixH/2} heure(s) au tarif horaire de 2.0 euros(s)",
			f"Le montant total à payer est de {PrixA + PrixH} euro(s)", sep="\n")
		else:
			print("Vous avez loué votre vélo pendant",
			 f"{PrixA} heure(s) au tarif horaire de 1.0 euros(s)",
			 f"{PrixH/2} heure(s) au tarif horaire de 2.0 euros(s)",
			 f"Le montant total à payer est de {PrixA + PrixH} euro(s)", sep="\n")


resultNcheck()

while check1 == False:
	i += 1

	if (HD+i) == (HF):
		check1 = True
		break

	if (HD+i) in Univers1:
		PrixA += 1
	elif (HD+i) in Univers2:
		PrixH += 2
	elif (HD+i) in Univers3:
		PrixA += 1
	else:
		check1 =  True

resultNcheck()