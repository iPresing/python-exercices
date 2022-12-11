
BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Veuillez rentrer une valeur : "))
sum = 0
NouvelleQuantite = 0
Qtf = " "
Check = False

print("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut :")

for sum in [fromage,eau,ail,pain]:

    if sum == fromage or sum == pain:
        if sum == fromage:
            Qtf = "gr de fromage"
        else:
            Qtf = "gr de pain"
    elif sum == eau and Check == False:
        Qtf = "dl d'eau"
        Check = True
    else:
        Qtf = "gousse(s) d'ail"
    nouvelleQuantite = ((sum *nbConvives)/BASE)

    print("- {} {}".format(nouvelleQuantite,Qtf))

