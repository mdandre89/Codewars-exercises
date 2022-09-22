def isValidWalk(w):
    if len(w)!=10:
        return False
    if w.count("n")==w.count("s") and w.count("e")==w.count("w"):
        return True
    else:
        return False