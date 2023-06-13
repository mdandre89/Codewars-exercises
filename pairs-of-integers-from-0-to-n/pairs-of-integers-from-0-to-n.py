def generate_pairs(n):
    t = []
    for i in range(n+1):
        for j in range(n+1):
            if i<=j:
                t.append([i,j])
    return t