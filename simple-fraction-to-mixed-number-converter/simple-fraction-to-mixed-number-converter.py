from fractions import Fraction
def mixed_fraction(s):
    sign = "" if s.count("-")%2==0 else "-"
    s = s.replace("-","")
    try:
        s = Fraction(s)
        if s.numerator ==0:
            return "0"
    except:
        raise ZeroDivisionError
    div = s.numerator//s.denominator
    modu = s.numerator%s.denominator
    if div == 0:
        return sign + str(modu) + "/" + str(s.denominator)
    return sign + str(div) + " " + str(modu) + "/" + str(s.denominator) if modu != 0 else sign + str(div) 