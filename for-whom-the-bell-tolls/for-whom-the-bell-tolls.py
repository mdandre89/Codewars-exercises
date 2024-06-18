def bell(n):
    ls = [(n-i)*(i+1) for i in range(n//2+n%2)]
    return ls + ls[:-1][::-1] if n%2==1 else ls + ls[::-1]