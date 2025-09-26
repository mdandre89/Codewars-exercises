import string
def caeser(message, key):
    out=[]
    word="abcdefghijklmnopqrstuvwxyz"
    num="0123456789"
    for l in message:
        l=l.lower()
        if l==" ":
            out.append(" ")
        elif l in string.punctuation or l in num:
            out.append(l)
        else:
            out.append(word[((word.index(l)+key)%26)].upper())   
    return "".join(out)