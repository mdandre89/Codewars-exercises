import re
def encode(strng):
    r = re.compile(r"([A-Z])\1*")
    return  "".join([str(m.end()-m.start())+m.group(1) for m in r.finditer(strng)])
    
def decode(strng): 
    ls = re.findall(r"[A-Z]+|[0-9]+",strng)
    return "".join([int(j)*ls[i+1] for i,j in enumerate(ls) if j.isdigit()])