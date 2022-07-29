dictio = {"{":"}","[":"]","(":")"}
def validBraces(s):
    y = 0
    while True:
        if len(s) == 2:
                return s[-1]==dictio.get(s[0],"")      
        if y > len(s):
            return False
        for i in range(1,len(s)+1):
            t = s[0:i]
            try:
                if t.count("{")==t.count("}") and t.count("[")==t.count("]") and t.count("(")==t.count(")") and dictio[s[0]] == s[i-1]:
                    s = s[1:i-1] + s[i:]
                    break
            except:
                return False
        y += 1