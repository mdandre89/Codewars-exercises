from fractions import Fraction as f
def game(n):
    return [f(n**2/2).numerator,f(n**2/2).denominator] if n%2 ==1 else [n**2/2]