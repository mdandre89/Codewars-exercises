import re
def increment_string(st):
    l = len(st)    
    if ret(st)==0:
        return st+"1"
    return st[:l-ret(st)] +str(int(st[-ret(st):])+1).zfill(ret(st))
    
def ret(s):
    try:
        return len(re.search(r"(\d)*$",s).group(0))
    except:
        return 0