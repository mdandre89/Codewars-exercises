import itertools
def encode_rail_fence_cipher(s, n):
    c  = itertools.cycle([i for i in range(1,n)] + [n] + [i for i in range(2,n)][::-1])
    t = sorted([[next(c),j] for i,j in enumerate(s)],key=lambda x:x[0])
    return "".join(i[1] for i in t)
    
def decode_rail_fence_cipher(s, n):
    c = itertools.cycle([i for i in range(1,n)] + [n] + [i for i in range(2,n)][::-1])
    t = [[next(c),i] for i in range(len(s))]
    s = itertools.cycle(s)
    for i in range(1,n+1):
        for k,z in enumerate(t):
            if z[0] == i:
                t[k][1] = next(s)
    return "".join(i[1] for i in t)    