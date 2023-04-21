def sqInRect(lng, wdth):
    if wdth>1 and lng == wdth :
        return None
    return square(lng,wdth)

def square(lng, wdth):
    if wdth > lng:
        wdth,lng =lng,wdth
    if lng==wdth:
        return [lng]
    return [wdth] + square(lng - wdth,wdth)