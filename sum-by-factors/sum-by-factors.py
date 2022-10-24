def sum_for_list(casa):
    lst = []
    mx = max(abs(min(casa)),abs(max(casa)))
    for i in range(2,mx+1):
        if any(abs(j)%i == 0 for j in casa) and i not in lst:
            if any(i%z == 0 for z in lst):
                continue 
            else:
                lst.append(i)
    lst.sort()
    for i,j in enumerate(lst):
        lst[i] = [j, sum([z for z in casa if z%j == 0])]
    return lst
    