import itertools
def addition_without_carrying(a,b):
    return int(''.join(str((int(i[0]) + int(i[1]))%10)  for i in itertools.zip_longest(str(a)[::-1] , str(b)[::-1], fillvalue='0'))[::-1])