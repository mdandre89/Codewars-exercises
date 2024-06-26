def fixed_xor(a, b):
    if not a or not b:
        return ''
    l=min(len(a), len(b))
    return '{0:0{1}x}'.format(int(a[:l], 16) ^ int(b[:l], 16), l)