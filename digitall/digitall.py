import re
def digit_all (x):
    try:
        return "".join(re.findall(r"[0-9]",x))
    except:
        return 'Invalid input !'