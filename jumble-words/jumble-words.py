import re
def jumble(stre):
    return re.sub(r"(\w)(\w*)(\w)",replacement,stre)
    
def replacement(s):
    s = s.group(0)
    if len(s)>3:
        return s[0] + s[-2] + s[1:-2] + s[-1]
    else:
        return s