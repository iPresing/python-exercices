# exercice3 #

a=int(input("Entrez la premiere  valeur : "))
b=int(input("Entrez la deuxieme  valeur : "))
c=int(input("Entrez la troisieme valeur : "))



print("Les valeurs entrees sont : a = " , a , ", b = ", b , " et c = " , c)
print("Permutation: a ==> b, b ==> c, c ==> a")




"""      *******************************************
         * Completez le programme a partir d'ici.
         *******************************************
"""
temp_1 = a

a = c
c = b
b = temp_1


"""     *******************************************
         * Ne rien modifier apres cette ligne.
         *******************************************
"""

print("Les valeurs permutees sont : a = " , a , ", b = ", b , " et c = " , c)