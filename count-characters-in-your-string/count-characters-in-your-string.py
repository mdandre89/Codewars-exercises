def count(strg):
    dictio = {}
    for i in strg:
        dictio[i] = dictio.get(i,0)+1
    return dictio