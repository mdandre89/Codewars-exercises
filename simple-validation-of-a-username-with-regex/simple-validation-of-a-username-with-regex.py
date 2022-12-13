import re,string

def validate_usr(us):
    t = re.findall(r'[a-z0-9_]{4,16}',us)
    if t and len(t[0])==len(us):
        return True 
    else:
        return False