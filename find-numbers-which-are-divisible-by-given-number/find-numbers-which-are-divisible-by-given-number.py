def divisible_by(numbers, divisor):
    set=[]
    for n in numbers:
        if n%divisor==0:
            set.append(n)
        else:
            pass
    return set