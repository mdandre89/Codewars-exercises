def get_two_complement_int(n):
    return int("".join([str(1^int(i)) for i in bin(n)[2:]]),2)+1