def sum_of_digits(digits): 
    if digits is None:
        return ""
    digits = str(digits)
    sm = sum(int(i) for i in digits)
    return " + ".join(i for i in digits) + " = " + str(sm)