from fractions import Fraction
def friendlyNumbers(m, n):
    m = Fraction(sum(i for i in range(1,m+1) if m%i==0),m)
    n = Fraction(sum(i for i in range(1,n+1) if n%i==0),n)
    return 'Friendly!' if m == n else "{} {}".format(m,n)