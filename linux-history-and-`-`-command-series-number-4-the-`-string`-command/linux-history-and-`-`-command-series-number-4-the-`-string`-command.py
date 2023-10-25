import re
def bang_start_string(s,history): 
    patt = re.findall(r"\d+  .*",history)
    for i in patt[::-1]:
        if " ".join(i.split()[1:]).startswith(s):
            return " ".join(i.split()[1:])
    return "!"+s+": event not found"
    