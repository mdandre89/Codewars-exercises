import re
def licence_plate(s):
    substitute = re.sub('[a-zA-Z]+(?![^0-9a-zA-Z]+|[a-zA-Z])|[^0-9a-zA-Z]+|[0-9]+(?![^0-9a-zA-Z]+|[0-9])', functio, s).upper().strip('-')[0:8].strip('-')
    return substitute if not substitute.isdigit() and len(substitute)>=2 else 'not possible'

def functio(a):
    print("match", a)
    if a.group().isdigit():
        return a.group() + '-'
    elif a.group().isalpha():
        return a.group() + '-'
    else:
        return '-'