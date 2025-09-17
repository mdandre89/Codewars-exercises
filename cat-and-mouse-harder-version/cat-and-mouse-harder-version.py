import re
def cat_mouse(x,j):
    if len(x.replace(".",""))<3:
        return 'boring without all three'
    if abs(x.index('m') - x.index('C'))<=j:
        if re.search(r'm\.*?D\.*?C|C\.*?D\.*?m',x):
            return 'Protected!'
        return "Caught!"
    return "Escaped!"