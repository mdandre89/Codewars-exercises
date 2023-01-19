import math
def decrypt(en, n):
    if n<=0:
        return en
    t = [0]*(len(en))
    z=0
    while z < n:
        for j,i in enumerate(en):
            if j <= len(en)/2-1:
                t[2*j+1]=i
            else:
                t[2*math.ceil(j-len(en)/2)]=i
        en = "".join(t)
        z += 1
    return "".join(t)
    
def encrypt(text, n):
    j = 0
    while j < n:
        text = text[1::2] + text[::2]
        j +=1 
    return text