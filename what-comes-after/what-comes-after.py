import re
def comes_after(st, l): 
    return ''.join(re.findall(rf'{l.lower()}(?=([^\W\d_]))', st, re.IGNORECASE))