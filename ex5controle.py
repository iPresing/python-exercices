def assurance(age, year, accident, ancient):
    
    if age == 0 or year > 2023 or accident < 0:
        return "Anomalie"
    
    conditions_red = [age < 25, (2023 - year) < 2, accident == 0]
    conditions_orange = [age < 25, (2023 - year) >= 2, accident == 0]
    conditions_vert =  [age >= 25, (2023 - year) >= 2, accident == 0]
    
    
    if all(conditions_vert):
        return "vert" if ancient < 1 else "bleu"
    elif accident == 1:
        return "orange" if ancient < 1 else "vert"
    elif accident == 2:
        return "rouge" if ancient < 1 else "orange"
    else:
        "refus"
        
    if all(conditions_orange):
        return "orange" if ancient < 1 else "vert" 
    elif accident == 1:
        return "rouge" if ancient < 1 else "orange"
    else:
        return "refus"
    
    if all(conditions_red):
        return "rouge" if ancient < 1 else "orange"
    else:
        return "refus"
    
    
    
        
    
        
        
print(assurance(27, 2022, 1, 2))
    
    
    