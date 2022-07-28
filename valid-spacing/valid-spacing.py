import re
def valid_spacing(s):
    return bool(re.search(r'^[A-z]+$', s)) or not bool(re.search(r' [ ]+|^ [A-z]*|[A-z]+ $|^[ ]+$', s))