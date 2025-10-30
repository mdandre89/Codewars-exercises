def flip_bit(value, bit_index):
    return value^(int(("1"+"0"*(bit_index-1)),2))