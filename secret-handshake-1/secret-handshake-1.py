dictio = {"wink":1,"double blink":10, "close your eyes":100, "jump":1000}

def handshake(n):
    t = []
    if type(n) == int:
        if n <= 0 or n> 31:
            return []
        try:
            n = bin(n)[2:]
        except:
            return []
    try:
        int(n,2)
    except:
        return []
    n = "0000" + n
    if n[-1]=="1":
        t.append("wink")
    if n[-2]=="1":
        t.append("double blink")
    if n[-3]=="1":
        t.append("close your eyes")
    if n[-4]=="1":
        t.append("jump")
    return t if n[-5] !="1" else t[::-1]

def code(ls):
    s = 0
    if ls ==[]:
        return "0"
    for i in ls:
        try:
            s += dictio[i]
        except:
            return "0"
    return str(s) if dictio[ls[0]] <= dictio[ls[-1]] else str(s+10000)