import math
def help_zoom(key):
    l = len(key)
    if int(math.sqrt(l)) != math.sqrt(l):
        return "No"
    l1 = int(math.sqrt(l))
    key  = [key[i:i+l1] for i in range(0,l,l1)]
    return "Yes" if key == [list(i) for i in list(zip(*list(zip(*key[::-1]))[::-1]))] else "No"