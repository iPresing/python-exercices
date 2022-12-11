def MultipleTable():
    multiplier = range(0, 10)
    multiplied = float(input("Vous cherchez la table de quel nombre ? "))

    for x in multiplier:
        print(f"{multiplied} * {x} = {round((multiplied * x), 1)}")
    MultipleTable()


MultipleTable()
