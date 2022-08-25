def square_or_square_root(arr):
    return [i**0.5 if int(i**0.5)==i**0.5 else i**2 for i in arr]