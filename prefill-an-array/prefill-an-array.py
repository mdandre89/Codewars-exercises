def prefill(n,v=None):
    try:
        n = int(n)
        if n < 0:
            raise TypeError
        if n ==0:
            return []
        return [v for i in range(n)]
    except:
        raise TypeError(str(n) +" is invalid")