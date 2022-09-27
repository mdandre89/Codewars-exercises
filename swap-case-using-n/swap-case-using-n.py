def swap(s,n):
    by_n, len_by_n = bin(n)[2:], len(bin(n)[2:])
    t, i = '', 0
    for j in s:
        if j.isalpha():
            t+= j.swapcase() if by_n[i%len_by_n]=='1' else j
            i+=1
        else:
            t+=j
    return t