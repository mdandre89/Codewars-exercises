import re
def insert_dash(num):
    return re.sub(r"[13579]{2,}",lambda m : "-".join(list(str(m.group()))),str(num))