def closest(lst):
    m = min(abs(i) for i in lst)
    if m in lst and -m in lst:
        return None if m!=0 else 0
    return m if m in lst else -m