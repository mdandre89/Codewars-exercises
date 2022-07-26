def vampire_test(x, y):
    for i in str(x)+str(y):
        if not str(x*y).count(i)==(str(x)+str(y)).count(i):
            return False
    return True