import operator
def persistence(n):
    n = str(n)
    y = 0
    while len(n)>1:
        n = str(reduce(operator.mul,[int(i) for i in n]))
        y +=1
    return y