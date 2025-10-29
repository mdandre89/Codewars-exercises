import random
def get_bingo_card():
    return data("B",5,1,15) + data("I",5,16,30) + data("N",4,31,45) + data("G",5,46,60) + data("O",5,61,75)
    
    
def data(s,l,n,m):
    ls = set()
    while len(ls)<l:
        ls.add(random.randint(n,m))
    return [s+str(i) for i in ls]