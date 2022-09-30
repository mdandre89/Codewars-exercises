import math
def sumDigits(number):
    number = math.fabs(number)
    return sum([int(i) for i in str(int(number))])