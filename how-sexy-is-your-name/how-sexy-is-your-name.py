def sexy_name(name):
    n = sum([SCORES.get(i,0) for i in name.upper()])
    if n <= 60:
        return 'NOT TOO SEXY'
    if n <=300 :
        return 'PRETTY SEXY'
    return 'VERY SEXY' if n<600 else 'THE ULTIMATE SEXIEST'