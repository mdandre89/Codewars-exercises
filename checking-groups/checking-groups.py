def group_check(s):
    l = len(s)
    i=0
    while i< l:
        s=s.replace("()","")
        s=s.replace("[]","")
        s=s.replace("{}","")
        i+=1
    return not bool(len(s))