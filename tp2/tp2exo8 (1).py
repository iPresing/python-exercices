x = float(input("Entrez un nombre décimal : "))

if x < -10 or x >= 3: # méthode du sandwitch
    print("x n'appartient pas à I")
elif (x == -1) or (x == 0):
    print("x n'appartient pas à I")
else:
    print("x appartient à I")
