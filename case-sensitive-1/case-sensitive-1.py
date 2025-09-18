import re
def case_sensitive(s):
    return [s==s.lower(),re.findall(r'[A-Z]',s)]