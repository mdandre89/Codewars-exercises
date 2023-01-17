def range_bit_count(a, b):
    return sum([bin(i).count('1') for i in range(a,b+1)])