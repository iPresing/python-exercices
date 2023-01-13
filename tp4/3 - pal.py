from math import * 

chara = "otto"
chara = ''.join([char for char in chara if not char.isdigit()])

if len(chara) % 2 != 0:
    int_part = chara[0:ceil(int(len(chara)/2) + 1)]
else:
    int_part = chara[0:int(len(chara)/2)]

verif = [char for char in int_part]
result_expected = [char for char in chara]

verif_2nd = verif
verif = verif[::-1]
if len(chara) % 2 != 0:
    if verif[0] == verif_2nd[ceil(int(len(chara)/2))]:
        verif_2nd.pop(ceil(int(len(chara)/2)))
verif_2nd.extend(verif)


if result_expected == verif_2nd:
    print(" c'est un palindrome !")
else:
    print("C'en est pas un !")




"""
for char in charset(int_part):
    verif.append(char)
"""

"""
[verif.append(char) for char in charset(int_part)]
[result_expected.append(char) for char in charset(chara)]




if result_expected == verif_2nd:
    print(" c'est un palindrome !")
"""
