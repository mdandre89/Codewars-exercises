from fractions import Fraction
def calculate_ratio(w,h):
    if w==0 or h==0:
        return 'You threw an error'
    return str(Fraction(w,h).numerator)+":" + str(Fraction(w,h).denominator) 