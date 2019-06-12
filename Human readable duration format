def format_duration(s):
    if not s:
        return "now"
    t = [[31536000,"year"],[86400,"day"],[3600,"hour"],[60,"minute"],[1,"second"]]
    ls = []
    for i in t:
        n = int(s//i[0])
        if n > 0:
            ls.append([n,i[1]])
        s%=i[0]
    if len(ls) == 1:
        return str(ls[-1][0]) + " "+ls[-1][1] + "s"*(ls[-1][0]>1)
    return  ", ".join(str(i[0]) + " "+i[1] + "s"*(i[0]>1) for i in ls[:-1])+ " and " + str(ls[-1][0]) + " "+ls[-1][1] + "s"*(ls[-1][0]>1)
