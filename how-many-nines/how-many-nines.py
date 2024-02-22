mapping = {1:0, 10:1} # populated with create_mapping, used to speed up calculation 


def create_mapping(m):
    if m == 1:
        return 0
    if m == 10:
        return 1
    if m in mapping:
        return mapping[m]
    power = len(str(m)) - 1 
    result = 9*create_mapping(10**(power-1)) + 10**(power-1)
    mapping[m] = result
    return result

def nines(n):
    if n == 1:
        return 0
    if n == 10:
        return 1
    power = len(str(n)) - 1 
    create_mapping(10**(power-1 + 1))
    if n in mapping:
        return mapping[n]
    
    s = 0
    array = [int(value) if value != '0' else int(value) for count,value in enumerate(str(n)) ]
    numbers = list(range(power, -1, -1))
    my_iter = iter(zip( array, numbers))
    for digit, exponent in my_iter:
        if digit != 9:
            s += digit*mapping[10**(exponent)]
        elif digit==9:
            if exponent == 0:
                s+=1
            else:
                next_digit, next_exponent  = next(my_iter)
                s += digit*mapping[10**(exponent)] + int(str(n)[power - next_exponent: ]) + 1
                break
    return s