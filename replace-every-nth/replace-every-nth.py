def replace_nth(text, n, old, new):
    if n<=0:
        return text
    return "".join([i.replace(old,new) if i==old and text[:j+1].count(old)%n==0 else i for j,i in enumerate(text)])