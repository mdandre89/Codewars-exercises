import re
def stock_list(listOfArt, listOfCat):
    if  not listOfArt or not listOfCat:
        return ""
    t = []
    for i in listOfCat:
        s = 0
        for j in listOfArt:
            if j.startswith(i):
                s += int(re.search(r"\d+",j).group(0))
        t.append( "(" + i + " : "+str(s)+ ")")
    return " - ".join(t)