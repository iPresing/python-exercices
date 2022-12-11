

##### ex 1 - A
n = int(input("Veuillez rentrer un entier : "))
sum = 0
for i in range(0,n+1):
    sum += i
    print(i)
print(sum)
##### ex 1 - B
n = 0

while n != 100:
    n = int(input("Veuillez rentrer une valeur entière :"))

print("fini")
##### ex 1 - C

def number():
    k = int(input("Veuillez rentrer un réel :"))
    while (k < 0 or k > 20) :
        print(" Nombre incorrect")
        k = int(input("Veuillez rentrer un réel :"))
    else:
        return k

v_10 = 0
v_105 = 0
v_15 = 0

n = []
for i in range(0,10):
    n.append(number())

for x in n:
    if x < 10:
        v_10 += 1
    elif x >= 15:
        v_15 += 1
    else:
        v_105 += 1
print(f"Le nombre de valeurs inférieur à 10 est {v_10}",
      f"Le nombre de valeurs superieur ou egale à 15 est {v_15}",
      f"Le nombre de valeurs superieur ou egale à 10 et inferieur à 15 est {v_105}", sep="\n")

##### ex 1 - D

n = int(input())
i = 0
k = 0
while k <= n:
    i += 1
    k += i
    print("La valeur de la somme actuelle est :",k,i)



print("Le nombre recherché est", i-1)


##### ex 2 ####
import time

n = int(input())

for i in range(0,n+1):
    time.sleep(0.2)
    print(n-i)

while n >= 0:
    time.sleep(0.2)
    print(n)
    n -= 1




