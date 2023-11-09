dictio = {0:[0],1:[1],2:[2,4,8,6],3:[3,9,7,1],4:[4,6],5:[5],6:[6],7:[7,9,3,1],8:[8,4,1,6],9:[9,1],10:[0]}
def last_digit(n1, n2):
    n1 = int(str(n1)[-1])
    return dictio[n1][(n2-1)%len(dictio[n1])] if n2!=0 else 1