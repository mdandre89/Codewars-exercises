from functools import reduce
import operator
def main_diagonal_product(mat):
    return reduce(operator.mul, (j[i] for i,j in enumerate(mat)))