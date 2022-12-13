import re

def simplify(poly):
    r = re.findall(r'([+-])?([0-9]+)?([a-z]+)',poly)
    dictio = {}
    for i in r:
        m = "".join(sorted(i[2]))
        if i[0] == "" or i[0] =="+":
            if i[1]:
                dictio[m] = dictio.get(m,0) + int(i[1]) 
            else:
                dictio[m] = dictio.get(m,0) + 1
        else:
            if i[1]:
                dictio[m] = dictio.get(m,0) - int(i[1]) 
            else:
                dictio[m] = dictio.get(m,0) - 1 
    ls2 = sorted(dictio.items(),key=lambda x: (len(x[0]),x[0]) )
    return '+'.join(str(j)+i for i,j in ls2 if j).replace("1","").replace("+-","-").replace("++","+").strip("+")