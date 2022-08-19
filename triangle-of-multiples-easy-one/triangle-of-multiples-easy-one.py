def mult_triangle(n):
    m = (n*(n+1)/2)**2
    l = sum(range(1,n+1,2))**2
    return [m,m-l,l]