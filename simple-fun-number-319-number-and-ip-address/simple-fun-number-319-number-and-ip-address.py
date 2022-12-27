pow2s=lambda s: str(sum(int(j)*(2**i) for i,j in enumerate(s)))
def number_and_IP_address(s):
    if '.' in s:
        return pow2s(''.join('{0:08b}'.format(int(i)) for i in s.split("."))[::-1])
    else:
        s = '{0:032b}'.format(int(s))
        return ".".join(pow2s(s[i:i+8][::-1]) for i in range(0, 32, 8))