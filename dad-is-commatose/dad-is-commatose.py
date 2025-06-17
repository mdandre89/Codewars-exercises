import re
def dad_filter(s):
    l = len(s)
    s = s.strip(",")
    for i in range(l-1):
        if ","*(l-i) in s:
            s= s.replace(","*(l-i),",")
        
    return s.strip().strip(",")