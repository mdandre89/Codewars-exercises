import re
def to_underscore(s):
    return re.sub(r"[A-Z]([a-z0-9])+",lambda x : x.group().lower()+"_",s)[0:-1] if type(s)== str else str(s)