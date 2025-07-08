def to_binary(n):
    return bin(n)[2:] if n >= 0 else bin(n + (1 << 32))[2:]