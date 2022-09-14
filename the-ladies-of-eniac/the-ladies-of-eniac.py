import re

def rad_ladies(name):
    return re.sub(r"[13579%$&/£?@]", "", name).upper()