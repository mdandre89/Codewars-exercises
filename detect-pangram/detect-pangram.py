import re

def is_pangram(s):
    return len(set(re.sub(r'\W+', '', s.lower()))) > 25