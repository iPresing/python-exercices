HeureDébut = int(input("Donnez l'heure de début de la location (un entier) : "))
HeureFin = int(input("Donnez l'heure de fin de la location (un entier) : "))
PriceUnit = 0
Qt = 0
DurationX = 0
DurationY = 0


def calcPrice(x,y):
    if (x < 7) or (x > 17):
        DurationX = 7 - x
        if DurationX < 0:
            DurationX = 24 - x






print(f"Pour cette location vous paierez {calcPrice(HeureDébut,HeureFin)} euros")


print(f"")