chiffre = int(input("Entrez un nombre entier: "))
even = False

def checkEven(): #fonction qui permet de déterminer si le nombre est pair
    if (chiffre % 2) == 0:
        even = True
        return "pair"
    else:
        return "impair"
    

if chiffre == 0:
    print("Le nombre est zéro (et il est pair)")
elif chiffre > 0:
    print("Le nombre est positif et", checkEven())
else:
    print("Le nombre est négatif et", checkEven())
