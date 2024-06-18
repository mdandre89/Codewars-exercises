def namelist(names):
    if len(names)==0:
        return ""
    elif len(names)==1:
        return names[0].get("name",0)   
    return ", ".join([ i["name"]  for i in names[:-1]]) + " & " + names[-1]['name']