def word_pattern(p, str):
    dictio = {}
    if len(p) != len(str.split(" ")):
        return False
    str  = str.split(" ")
    for i,j in enumerate(p):
        if j not in dictio:
            dictio[j] = str[i]
        elif dictio[j] != str[i]:
            return False
    return len(set(dictio.keys())) == len(set(dictio.values()))