import string
def to_nato(words):
    t = []
    dictio = {"A":"Alfa","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot",
    "G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike",
    "N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra",
    "T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"Xray","Y":"Yankee","Z":"Zulu"," ":""}
    for l in words:
        if l in string.punctuation:
            t.append(l)
        elif l==" ":
            pass
        else:
            t.append(dictio.get(l.upper(),""))
    return " ".join(t)   