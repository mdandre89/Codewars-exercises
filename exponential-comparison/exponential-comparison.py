from math import log
def compare(number1, number2):
    base1, exp1 = number1
    base2, exp2 = number2 
    return number1 if (exp1/exp2)*log(base1)/log(base2)>1 else number2