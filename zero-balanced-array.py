def is_zero_balanced(arr):
    return sorted(arr)[::-1] == [-i if i!=0 else 0 for i in sorted(arr)] and len(arr) >0