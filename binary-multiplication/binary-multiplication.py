def bin_mul(n,m):
    n, m = bin(max(n,m))[2:], min(n,m)
    return  [m*(2**i) for i,j in enumerate(n[::-1]) if j=="1"][::-1] if m!=0 and n!=0 else []