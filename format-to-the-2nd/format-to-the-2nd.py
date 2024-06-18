def print_nums(*args):
    stringa = ""
    if len(args) == 0:
        return ""
    elif len(args) == 1:
        return str(args[0])
    else:
        for i in args:
            stringa += "0"*(len(str(max(args))) - len(str(i))) + str(i)+"\n"
            
    return stringa.rstrip("\n")