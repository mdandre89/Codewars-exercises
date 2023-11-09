def pipe_fix(numbers):
    n=min(numbers)
    m=max(numbers)
    l=[]
    i=n
    while i<=m:
        l.append(i)
        i=i+1
    return l