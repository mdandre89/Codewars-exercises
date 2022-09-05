import re
def cowboys_dollars(boots):
    botlef = re.findall(r"\[\(1\)\]",boots[0][0:boots[0].index("&")])
    botrgt = re.findall(r"\[\(1\)\]",boots[1][0:boots[1].index("&")])
    return "This Rhinestone Cowboy has "+str(len(botrgt))+ " dollar bills in his right boot and "+str(len(botlef))+" in the left"