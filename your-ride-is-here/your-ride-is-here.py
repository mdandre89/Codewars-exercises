import string
from functools import reduce
def ride(group,comet):
    g = reduce((lambda x, y: x * y),map(lambda x:string.ascii_lowercase.index(x.lower())+1,list(group)))%47
    c = reduce((lambda x, y: x * y),map(lambda x:string.ascii_lowercase.index(x.lower())+1,list(comet)))%47
    return "GO" if g==c else "STAY"