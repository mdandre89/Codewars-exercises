def valid_parentheses(strin):
    if strin.count("(")!=strin.count(")"):
        return False
    coun = 0
    councl = 0
    for i in strin:
        if i=="(":
            coun +=1
        elif i==")":
            councl +=1
        else:
            pass
        if coun < councl:
            return False
    return True