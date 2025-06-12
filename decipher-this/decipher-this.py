import re
def decipher_this(string):
    t = []
    for i in re.findall(r"((\d+)(\w*))",string):    
        if len(i)>2 and len(i[2]) == 1:
            t.append(chr(int(i[1])) + i[2])
        elif len(i)>2 and i[2]=='':
            t.append(chr(int(i[1])))  
        else:   
            t.append(chr(int(i[1])) + i[2][-1]+i[2][1:-1] + i[2][0])
    return " ".join(t)