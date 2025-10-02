import re
def string_parse(st):
    try:
        return re.sub(r'((\w)\2*)',lambda i: i.group(0) if len(i.group(0))<=2 else i.group(0)[:2] +"["+i.group(0)[2:]+"]",st)
    except:   
        return "Please enter a valid string"