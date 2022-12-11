import random


def reason():
    if guess > value:
        return "plus grande"
    elif guess < value:
        return "plus petite"
    else:
        return "correcte"

value = random.randint(0, 100)
print(value)

guess = -5
n = 0
while guess != value:
    guess = int(input("Veuillez choisir une valeur :"))
    n += 1
    print(f"La valeur choisie est {reason()}", f"{n} essai(s)", sep="\n")
