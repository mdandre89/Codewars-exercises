import re
def bang_bang(history): 
    return " ".join(re.findall(r"\d+  .*",history)[-1].split()[1:])
  