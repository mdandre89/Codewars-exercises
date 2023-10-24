def logistic_map(w,h,xs,ys):
    return [[min((abs(z-i) + abs(k-j) for k,z in zip(xs,ys))) if xs and ys else None for j in range(w)] for i in range(h)]        