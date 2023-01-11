def check(jour, mois, annee, date, bis = False):
	if len(date) != 8:
		return print("date incorrecte la date excède 8 caractères"), catcherror()
	if ((annee % 4 == 0) and (annee % 100 == 0)) or (annee % 400):
		bis = True
	if bis and (mois == 2):
		return print("date incorrecte") if (jour > 29) else print("date correcte")
	else:
		return print("date incorrecte") if (jour > 31) or (mois > 12) else print("date correcte")


def catcherror():
	date = input("Veuillez rentrer la date sous la forme jjmmaaaa : ")

	mois = int(date[2:4])
	jour = int(date[0:2])
	annee = int(date[4:8])

	check(jour, mois, annee, date)

date = input("Veuillez rentrer la date sous la forme jjmmaaaa : ")

mois = int(date[2:4])
jour = int(date[0:2])
annee = int(date[4:8])


check(jour, mois, annee, date)

