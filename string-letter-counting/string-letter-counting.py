import re
from collections import Counter
def string_letter_count(s):
    c = Counter(re.sub(r'[^a-zA-Z]','',s).lower())
    s = ''
    for l in sorted(c.items(), key=lambda item: (item[0])):
        s += str(l[1]) + l[0]
    return s