import re
def validate_bet(game, text):
    try:
        t = sorted(int(i) for i in re.sub(r'(\d)([ ,]+?)+',r"\1 ", text).split(" ")) 
        return t if len(set(t)) == game[0] == len(t) and t[-1] <= game[1] and t[0]>0 else None
    except:
        return None