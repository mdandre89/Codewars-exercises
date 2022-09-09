scoring = {"accounts" : 1,
"finance" : 2, 
"canteen" : 10,
"regulation" : 3,
"trading" : 6,
"change" : 6,
"IS" : 8,
"retail" : 5,
"cleaning" : 4,
"pissing about" : 25}

def boredom(staff):
    tot = 0
    for i in list(staff.values()):
        tot += scoring[i]
    if tot > 99:
        return 'party time!!'
    elif tot < 81:
        return 'kill me now'
    else:
        return 'i can handle this'
        
    return tot