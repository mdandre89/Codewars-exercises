import hashlib
from datetime import datetime

def geohash(dow, date=datetime.now()):
    dictio = "abcdef"
    s = "-".join(map(lambda x : str(x),[date.year,"{0:0>2}".format(date.month),"{0:0>2}".format(date.day)]))+"-"+format(dow,'.2f')
    c = computeMD5hash(s)
    ls = sum([(10+dictio.index(j))*16**(-i-1) if j in dictio else int(j)*16**(-i-1) for i,j in enumerate(str(c)[:16])])
    ls2 = sum([(10+dictio.index(j))*16**(-i-1) if j in dictio else int(j)*16**(-i-1) for i,j in enumerate(str(c)[16:])])
    return [round(ls,6),round(ls2,6)]
    
def computeMD5hash(mystring):
    m = hashlib.md5()
    m.update(mystring.encode('utf-8'))
    return m.hexdigest()