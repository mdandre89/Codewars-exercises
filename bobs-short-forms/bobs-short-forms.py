import re
def short_form(s):
    return s[0]+re.sub(r"[aeiouAEIOU]","",s[1:-1]) + s[-1]