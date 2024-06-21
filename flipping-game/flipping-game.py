def flipping_game(ls):
    M = N = sum(ls)
    if len(ls)==N:
        return N-1 
    for i in range(len(ls)+1):
        for j in range(i):
            l = N + i - j - 2*sum(ls[j:i]) 
            if M < l:
                M = l
    return M 