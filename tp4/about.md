tp4ex4 (without counts) :

Ce code demande à l'utilisateur d'entrer un nombre entier (Range), qui détermine la plage de valeurs dans laquelle les nombres de la liste L1 peuvent être choisis aléatoirement. Ensuite, il génère une liste L1 de 11 nombres aléatoires compris entre 1 et Range (inclus).

Il crée ensuite un dictionnaire (counts) qui compte le nombre d'occurrences de chaque nombre dans la liste L1. Pour chaque nombre n dans L1, s'il est déjà présent dans le dictionnaire counts, son compte (count) est incrémenté de 1, sinon un nouvel entrée est ajoutée au dictionnaire avec un compte de 1.

Enfin, le code parcourt le dictionnaire counts et recherche le nombre (num) ayant le plus grand compte (count). Si un nombre est trouvé avec un compte supérieur au compte maximum actuel (max_count), alors max_count et max_num sont mis à jour avec le compte et le nombre correspondants. En fin de boucle, max_num contient le nombre le plus fréquent de la liste L1, et max_count contient son nombre d'occurrences. Ces deux valeurs sont finalement affichées.
