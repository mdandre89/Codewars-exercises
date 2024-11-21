import re
def disemvowel(string):
    return "".join(re.findall(r"[^aeiuoAEIOU]",string))