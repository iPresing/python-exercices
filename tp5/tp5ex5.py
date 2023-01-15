def fiche_paye(salaire, heures, last_hours = 0):
    conditions = [heures >= 160, heures >= 200]
    
    if all(conditions):
        first_hours = 160 * salaire
        scnd_hours = (200 - 161) * salaire * 1.25
        last_hours = (heures - 200) * salaire * 1.50
    elif conditions[0]:
        first_hours = 160 * salaire
        scnd_hours = (heures - 161) * salaire * 1.25
    else:
        first_hours = heures * salaire
        
    somme = first_hours + scnd_hours + last_hours
    return print(f"En {heures} de travail l'employé a un salaire estimé à {somme} euro(s)")
        
        
        
sal_horaire = int(input("Salaire horaire : "))
heures = int(input("Temps de travail : "))

fiche_paye(sal_horaire, heures)
