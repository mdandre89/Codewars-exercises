from itertools import zip_longest
def transpose_two_strings(arr):
    return '\n'.join(i + ' ' + j for i,j in zip_longest(list(arr[0]), list(arr[1]), fillvalue=' ' ))