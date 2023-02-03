import re

def travel(r, zipcode):
    if zipcode not in r:
        return zipcode + ":/"
    t = re.findall(r"(\d*) ([A-Za-z. ]*) ([A-Z]{2,2} \d{5,5})",r)
    s = zipcode + ":"
    for i in t:
        if zipcode in i:
            s += i[1] + "," 
    s = s
    s = s.rstrip(",")  + "/"       
    for i in t:
        if zipcode in i:
            s += i[0]+","
    return s.rstrip(",")