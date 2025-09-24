def shifted_diff(first, second):
    l = len(first)
    if first == second:
        return 0
    else:
        for i in range(l):
            if first==second[l-i:]+second[:l-i]:
                return l-i
    
    return -1