import random

Range = 0
while Range <= 0:
        Range = int(input("Jusqu'à quelle valeur la liste peut s'étendre ? : "))

#L1 = [2, 8, 5, 6, 8, 3, 3, 3, 3, 8, 6]
L1 = [random.randint(1, Range) for _ in range(11)]
print(L1)

# Créer un dictionnaire qui compte le nombre d'occurence de chaque digit dans la liste
counts = {}
for n in L1:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1

# Trouver le digit le plus fréquent
max_num = None
max_count = 0
for num, count in counts.items():
    if count > max_count:
        max_num = num
        max_count = count

print("le nombre le plus frequent dans la liste est le : {} ({} x)".format(max_num, max_count))
