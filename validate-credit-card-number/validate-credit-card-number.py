def validate(n):    
    ls = [int(j)*2 if i%2==1 else int(j) for i,j in enumerate(str(n)[::-1])]
    r = sum([i if i<=9 else i-9 for i in ls])
    return True if r%10==0 else False        