import re
def encode(strng):
    r = re.compile(r"(\w)\1*")
    return  "".join([m.group(1)+str(m.end()-m.start()) for m in r.finditer(strng)])