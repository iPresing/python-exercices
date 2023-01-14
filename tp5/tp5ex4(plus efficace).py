"""
l'opérateur // est vachement utile dans cet exemple car il prend en compte uniquement la partie entière de la division , 
l'opérateur % lui prend le reste 

exemple 624 :

624 // 100 - > 6
reste = 624 % 100 = 624 - (6.xxx * 100) = 70
etc.




"""




def calculer_billets(montant):
    billets_100 = montant // 100
    reste = montant % 100
    billets_50 = reste // 50
    reste = reste % 50
    billets_10 = reste // 10
    reste = reste % 10
    billets_2 = reste // 2
    billets_1 = reste % 2
    return billets_100, billets_50, billets_10, billets_2, billets_1

montant = int(input("Entrez une somme d'argent: "))
billets_100, billets_50, billets_10, billets_2, billets_1 = calculer_billets(montant)

print(f'{billets_100} billets de 100')
print(f'{billets_50} billets de 50')
print(f'{billets_10} billets de 10')
print(f'{billets_2} billets de 2')
print(f'{billets_1} billets de 1')
