def seq_to_one(n):
    return list(range(1,n+1))[::-1] if n>1 else list(range(n,2))