import re
def reverse(str):
    return re.sub(r'((\w)\2{1,})',f, str)
    
def f(match):
    if match.group().isupper():
        return match.group().lower()
    return match.group().upper()