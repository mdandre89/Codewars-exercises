import re
def has_subpattern(s):
    r = re.findall(r'^([a-zA-Z0-9]+)\1+$',s)
    return bool(r)