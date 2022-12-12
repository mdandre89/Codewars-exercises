import re
def pig_latin(s):
    if not s or re.search(r'[^A-z]+', s, re.IGNORECASE):
        return None
    
    if s[0].lower() in 'aeiou':
        return s.lower() + 'way'
    elif not re.search(r'[aeiou]', s, re.IGNORECASE):
        return s.lower() + 'ay'
    else:
        first = re.search(r'^[^aeiou]+', s, re.IGNORECASE)
        second = re.search(r'[aeiou].*', s, re.IGNORECASE)
        return second.group().lower() + first.group().lower() + 'ay'