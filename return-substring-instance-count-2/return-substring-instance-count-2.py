import re
def search_substr(s, x, allow_overlap=True):
    if not s or not x:
        return 0
    if not allow_overlap:
        return len(re.findall(x,s)) if s and x else 0
    return sum( 1 for i in range(len(s)-len(x)+1) if s[i:i+len(x)]==x  )