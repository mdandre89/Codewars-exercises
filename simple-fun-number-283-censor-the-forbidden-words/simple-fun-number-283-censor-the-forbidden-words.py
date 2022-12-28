import re
def censor_this(t, f_w):
    for i in f_w:
        r = r'\b{0}\b'.format(i)
        t = re.sub(r,len(i)*"*",t,flags=re.I)
    return t