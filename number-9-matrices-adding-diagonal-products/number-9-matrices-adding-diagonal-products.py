from functools import reduce

def sum_prod_diags(matrix):
#   this one helped me out https://www.codewars.com/kata/5592dd43a9cd0e43a800019e/python
    l = len(matrix)
    if l == 1:
        return matrix[0]
    right =  [[ matrix[j][ (i + j)] for j in range(l-i)] for i in range(l)]
    right1 = [[ matrix[i+j][j] for j in range(l-i)] for i in range(1,l)]
    left =   [[ matrix[j][ l-j-1-i] for j in range(l-i)] for i in range(l)]
    left1 =  [[ matrix[i+j][l-j-1] for j in range(l-i)] for i in range(1,l)]
    
    s_r = [reduce(lambda x, y: x * y, diag, 1) for diag in right]
    s_r1 = [reduce(lambda x, y: x * y, diag, 1) for diag in right1]
    s_l = [reduce(lambda x, y: x * y, diag, 1) for diag in left]
    s_l1 = [reduce(lambda x, y: x * y, diag, 1) for diag in left1]
    
    return sum(s_r) + sum(s_r1) - sum(s_l) - sum(s_l1)