import re
def to_camel_case(text):
    if text == "":
        return ""  
    else:
        t = re.findall(r"[A-Za-z]+",text)
        t = [t[0]]+ [i.capitalize() for i in t[1:]]
        return "".join(t)