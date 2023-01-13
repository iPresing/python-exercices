nom = str.upper(input("Votre nom : ")) 
firstname = str.capitalize(input("Votre prénom : "))

nom_2 = str.upper(input("Votre nom : ")) 
firstname_2 = str.capitalize(input("Votre prénom : "))


print(f"{firstname} {nom}", f"{firstname_2} {nom_2}",sep="\n") if nom < nom_2 else print(f"{firstname_2} {nom_2}", f"{firstname} {nom}",sep="\n") if nom > nom_2 else print(f"{firstname} {nom}", f"{firstname_2} {nom_2}",sep="\n")

