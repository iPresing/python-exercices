chaine = input("Veuillez entrer votre chaîne de caractères : ")

def len_rework(str, u = 0):
    str_list = [a for a in str]
    #print(str_list)
    try:
        while str_list[u]:
            u += 1
    except IndexError:   #attrape l'erreur et redirige le stdrr en fonction...
        return int(u)
        
def voyelle(str, u = None,voy_number = 0):
    voy = ["a","e","i","o","u","y"]
    u= len_rework(str)
    str_list = [a for a in str]
    for p in range(u): voy_number += 1 if str_list[p] in voy else 0 
    return float(voy_number/u * 100)
    
    
def test_wagon(str, test="wagon"):
    if test in str:
        print("ok")
    
        
    
    
longueur, voyelle = len_rework(chaine), voyelle(chaine)

print(longueur, voyelle)

test_wagon(chaine)