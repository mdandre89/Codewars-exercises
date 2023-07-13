def is_narcissistic(i):
    j=len(str(i))
    n=1
    t=0
    while n<=j:
        c=str(i)[n-1]
        t=t+int(c)**j
        n=n+1
    if t==i:
        return True
    else:
        return False