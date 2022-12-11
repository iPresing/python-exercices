import random

token = random.randint(0,100)
print(str(token))

if (token / 50) <= 1:
    print("Pile!")
else:
    print("Face!")
    
