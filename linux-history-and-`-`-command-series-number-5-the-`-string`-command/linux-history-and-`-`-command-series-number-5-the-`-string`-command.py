import re
def bang_contain_string(s,history):
    t = [" ".join(i.split()[1:]) for i in re.findall(r"\d+  .*",history)[::-1]]
    for i in t:
        if s in i:
            return i
    return "!"+s+": event not found"