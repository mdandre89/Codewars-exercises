def score_throws(radiuses):
    s = sum(scora(i) for i in radiuses)
    return s if s!=10*len(radiuses) or not radiuses else 100+s

def scora(p):
    if p > 10:
        return 0
    return 10 if p < 5 else 5