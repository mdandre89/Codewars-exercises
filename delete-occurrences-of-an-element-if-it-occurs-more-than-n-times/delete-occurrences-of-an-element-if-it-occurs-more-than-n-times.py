def delete_nth(order,e):
    t = []
    for j,i in enumerate(order):
        if order[:j+1].count(i)<e+1:
            t.append(i)
    return t