import re
def bracket_buster(string):
    t = []
    try:    
        for i in re.findall(r"\[[A-Za-z '[:;<=>?@\\^_`{|}~0123456789-]*\]",string):
            t.append(i[1:-1])
        return t
    except:
        return "Take a seat on the bench."