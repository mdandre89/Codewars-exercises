import re
from string import ascii_lowercase as c
def missing_alphabets(s):
    s = "".join(sorted(s))
    try:
        l = max(map(lambda x: len(x),(i[0] for i in re.findall(r"(([a-z])\2{1,})",s))))
    except:
        l = 1
    return ''.join([i*(l-s.count(i)) for i in c if  i*l not in s  ])