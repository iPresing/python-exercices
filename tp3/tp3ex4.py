while True:

    print(" Veuillez rentrer :", "1 : Si vous voulez une structure itératif en for", "2 : Si vous préférez via une boucle while", sep="\n",end="\n")
    ch = int(input(" Votre choix : "))
    n = int(input("Veuillez rentrer la valeur : "))
    fact = 1

    if n == 0:
        print(f"Le factoriel de {n} est {fact}")

    if ch == 1:

        for i in range(0,n):
            fact *= (n-i)
        print(fact)

    elif ch == 2:
        i = 0
        k = n
        while ((n-i)) != 0:
            fact *= (n-i)
            i += 1
        print(fact)

    else:
        print("Je ne reconnais pas la méthode demandée veuillez choisir un nombre entre 1 et 2", end="\n")



