import re
def bang_n(n,history): 
    patt = re.findall(r"\d+  .*",history)
    return " ".join(patt[n-1].split()[1:]) if n <= len(patt) else "!"+str(n) + ": event not found"