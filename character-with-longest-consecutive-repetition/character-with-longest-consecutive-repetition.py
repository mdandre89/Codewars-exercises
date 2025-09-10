import string, re
def longest_repetition(chars):
    if not chars:
        return ('', 0)
    m = max(re.finditer(r"(.)\1*",chars),key=lambda x: len(x.group()))
    return (m.group()[0],len(m.group()))