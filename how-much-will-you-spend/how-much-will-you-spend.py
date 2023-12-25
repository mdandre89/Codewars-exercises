def getTotal(costs, items, tax):
    c = 0
    for i in items:
        c+= costs.get(i,0)
    return round(c*(1+tax),2)