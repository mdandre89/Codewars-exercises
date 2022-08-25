def title_case(*sd):
    if len(sd)<1 or sd[0]=="":
        return ""
    if len(sd)==2:
        tite, m = sd
        return " ".join([tite.split()[0].title()]+[i.title() if i.lower() not in [j.lower() for j in m.split()] else i.lower() for i in tite.split()[1:]])
    else:
        tite = sd[0]
        return " ".join([i.capitalize() for i in tite.split()])