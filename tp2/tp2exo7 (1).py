import random

token = random.randint(0,100)
print(str(token))


def odd():
    check = random.randint(1,3)
    return check
    

if odd() > 1 : # la condition test sur token inutile
    print("Pile!")
else:
    print("Face!")
    
