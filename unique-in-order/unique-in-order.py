import re
def unique_in_order(s):
    try:
        return [int(i) for i in re.findall(r"([A-Za-z0-9])\1*","".join(map(str,s)))]
    except:
        return re.findall(r"([A-Za-z0-9])\1*","".join(map(str,s)))