import re
def count_vowels(s = ''):
    if isinstance(s,str):    
        return len(re.findall(r"[AEIOUaeiou]",s))
    return None