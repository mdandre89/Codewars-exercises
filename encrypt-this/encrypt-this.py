import re
def encrypt_this(s):
        s = re.sub(r'[A-Za-z]+',change,s)
        return re.sub(r'[ ]{2,}'," ",s).strip(" ") if len(s) > 0 else ""
        
def change(s):
    s = s.group()
    if len(s) == 1:
        return str(ord(s))
    if len(s) == 2:
        return str(ord(s[0])) + s[1]
    return str(ord(s[0])) + s[-1] + s[2:-1] + s[1]