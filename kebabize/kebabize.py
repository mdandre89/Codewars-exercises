import string

def kebabize(stringa):
    newstring = ""
        
    for i in stringa: 
    
        if i.isdigit():
            pass
            
        elif i.islower():
            newstring += i
            
        else: 
            newstring += "-" + i.lower()
            
    if newstring.startswith("-"):
        return newstring[1:]
    else:
        return newstring