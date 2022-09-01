import re
def area_code(text):
    pattern = re.compile(r'(\(\d\d\d\))')
    mo1 = pattern.search(text)
    
    return mo1.group(0).strip("()")