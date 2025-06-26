import string
def duplicate_count(text):
    t = []
    for a in string.printable:
        if text.lower().count(a)>1:
            t.append(a)   
    
    return len(t) if len(t)>0 else 0