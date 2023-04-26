import re
def key_strokes(keys):
    mg = ["QWERTYUIOP", "ASDFGHJKL;'","ZXCVBNM,.?"]
    s = ""
    for i in keys:
        if i[1]<3:
            s += mg[i[1]][i[0]].lower()
        elif 1<i[0]<=6:
            s += " "
        else: 
            pass
    s = s.capitalize().replace(" i "," I ")
    s = re.sub(r"\.[,'; ]*?\s*?[,'; ]*?\s*?[a-z]|\?[,'; ]*?\s*[,'; ]*?\s*?[a-z]",lambda x: x.group().upper(),s)
    s = re.sub(r"\.[,';]*?[a-z]|\?[,';]*?[a-z]",lambda x: x.group().upper(),s)
    s = re.sub(r" [,';]*?i[,';]*? | i | i\b|[,'; ]+i[,'; ]+|[,'; ]+i[?.]",lambda x: x.group().replace("i","I"),s)
    return s