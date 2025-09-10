def isomorph(a, b):
    dictio = {}
    for i,j in enumerate(a):
        if j in dictio and dictio[j] != b[i]:
            return False
        dictio[j] = b[i]
    return len(set(dictio.keys())) == len(set(dictio.values())) and len(a) == len(b)