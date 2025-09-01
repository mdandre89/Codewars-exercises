def crap(garden, bags=0, cap=0):
    c = "".join(["".join(i) for i in garden]).count("@")
    if "".join(["".join(i) for i in garden]).count("D")>0:
        return "Dog!!"
    return "Clean" if bags*cap>= c else "Cr@p"