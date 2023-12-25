def format_duration(se):
    if se == 0:
        return "now"
    y = se/31536000
    d = (se%31536000)/86400
    h = ((se%31536000)%86400)/3600
    m = (((se%31536000)%86400)%3600)/60
    s = (((se%31536000)%86400)%3600)%60
    ls = [y,d,h,m,s]
    ls2 = [str(y)+" year",str(d)+" day",str(h)+" hour",str(m)+" minute",str(s)+" second"]
    t = []
    for i in range(len(ls)):
        if ls[i]>1:
            t.append(ls2[i] +"s")
        elif ls[i]==1:
            t.append(ls2[i])
    if len(t)==1:
        return t[0]
    return ", ".join(t[:-1]) + " and " + t[-1]