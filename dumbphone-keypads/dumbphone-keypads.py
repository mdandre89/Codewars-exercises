dictio = dict(zip("1234567890 *#ABCDEFGHIJKLMNOPQRSTUVWXYZ",["1","2222","3333","4444","5555","6666","77777","8888","99999","00","0","*","#","2","22","222","3","33","333","4","44","444","5","55","555","6","66","666","7","77","777","7777","8","88","888","9","99","999","9999"]))
from itertools import groupby 
def sequence(phrase):
    phrase = [dictio[i] for i in phrase.upper()]
    return "".join(["p".join(str(i) for i in i[1]) for i in groupby(phrase,key=lambda x: x[0])])