def highest_value(a, b):
    def transform(stringa):
        tot = 0
        for i in stringa:
            tot += ord(i)
        return tot
    if transform(a) >= transform(b):    
        return a
    else:
        return b