def countBits(n):
    return sum(1 for i in bin(n)[2:] if i == '1')