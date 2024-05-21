from itertools import cycle
def numeric_formatter(template, num = 1234567890):
    s = ''
    itera = cycle(str(num))
    for i in template:
        if i.isdigit():
            s+=i
        elif i.isalpha():
            s+=next(itera)
        else:
            s+=i
    return s