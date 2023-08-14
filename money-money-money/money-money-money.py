def calculate_years(principal, interest, tax, desired):
    y = 0
    res = principal
    while res < desired:
        res = res*(interest*(1-tax)+1)
        y += 1
    return y 