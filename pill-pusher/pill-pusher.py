def prescribe(d,a,b):
    n = d//a
    m = n*a
    for i in range(n+1):
        new_m = (n-i)*a + (d - (n-i)*a)//b *b
        if new_m >= m and new_m <= d:
            m = new_m
    return m
        