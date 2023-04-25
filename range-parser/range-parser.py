def range_parser(s):
    t = []
    for i in s.split(","):
        if "-" in i:
            if ":" in i:
                ran = range(int(i.split("-")[0]),int(i.split("-")[1].split(":")[0])+1,int(i.split("-")[1].split(":")[1]) )
            else:
                ran = range(int(i.split("-")[0]),int(i.split("-")[-1])+1 )
            t += ([j for j in ran])
        else:
            t+= ([int(i)])
    return t