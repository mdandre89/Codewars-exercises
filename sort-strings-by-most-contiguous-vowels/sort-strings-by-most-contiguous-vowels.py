import re
def sort_strings_by_vowels(seq): 
    return sorted(seq, key=lambda x: len(max(re.findall(r'[AEIOUaeiou]+', x) or [''], key=len)) , reverse=True) 