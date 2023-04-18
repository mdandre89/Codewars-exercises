def is_digit(n):
    try:
        int(n)
        return True if 0<=int(n)<10 and n.isdigit() else False
    except:
        return False