dico = {}
dicob = {}
binome = {}


def pairing(p_key, val=[]):
    val = []
    [val.append(binome[p_key][k]) for k in ('firstname', 'name', 'group')]
    return val


""" Première partie du code (question 5)
dico['firstname']= input('Quel est ton prénom : ')
dico['name'] = input('Quel est ton nom : ')
dico['promo'] = 'RT'
dico['group'] = 'RT122'


def call(input): #pas très utile cependant ...
    return dico[input]

#print('votre nom est {}, prénom est {}; vous faites partie de la promo {} et votre groupe est {}'.format(dico['name'],dico['firstname'],dico['promo'],dico['group']))
print('votre nom est {}, prénom est {}; vous faites partie de la promo {} et votre groupe est {}'.format(call('name'),call('firstname'),call('promo'),call('group')))
"""

dico['firstname']= 'Timothée'
dico['name'] = 'TREPIER'
dico['promo'] = 'RT'
dico['group'] = 'RT122'

dicob['firstname']= 'Corentin'
dicob['name'] = 'MOUROT'
dicob['promo'] = 'RT'
dicob['group'] = 'RT122'

binome["68000"] = dico
binome["97214"] = dicob

print("Les clés du dictionnaire sont : ", end="\n")
[print(f'-{keys}', end="\n") for keys in dico.keys()]
print("Les valeurs du dictionnaire sont : ", end="\n")
[print(f'-{values}', end="\n") for values in dico.values()]   
print("Les tuplets du dictionnaire sont : ", end="\n")
[print(f'-{x}', end="\n") for x in dico.items()]
#[print(f'-{x}:{y}', end="\n") for x,y in dico.items()] #format un peu différent ...




#[print(binome[u][k]) for u in list(binome.keys()) for k in ('firstname', 'name', 'group')]

print("Les étudiants formant le binôme sont : ", end="\n")
for u in list(binome.keys()):
    val = pairing(u)
    print(f"- L'étudiant {val[0]} {val[1]} du groupe {val[2]}")
