import re
def remove_chars(s):
    return "".join(re.findall(r'[A-Za-z ]',s))