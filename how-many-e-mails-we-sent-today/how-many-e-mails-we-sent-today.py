import math
def get_percentage(sent, limit=1000):
    if sent == 0:
        return "No e-mails sent"
    return "{}%".format(math.floor(sent/limit*100)) if sent < limit else "Daily limit is reached"