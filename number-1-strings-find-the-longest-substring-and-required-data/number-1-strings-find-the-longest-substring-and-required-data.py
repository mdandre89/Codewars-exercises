import re
def find_longest_substr(s):
    m = 0
    t = ()
    for i in re.finditer(r'(([a-zA-Z0-9])\2*)',s):
        if len(i.group())>m:
            m = len(i.group())
            t = (str(ord(i.group()[0])),[i.start(),i.end()-1])
    return [t[0],m,t[1]]