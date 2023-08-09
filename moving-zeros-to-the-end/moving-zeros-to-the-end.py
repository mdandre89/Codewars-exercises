def move_zeros(array):
    l2 = [i for i in array if i==0 and i is not False]
    return [i for i in array if i!=0 or i is False]+l2