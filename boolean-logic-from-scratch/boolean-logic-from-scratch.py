def func_or(a,b):
    return not(not a and not b)

def func_xor(a,b):
    return (not(a and b) and func_or(a,b))