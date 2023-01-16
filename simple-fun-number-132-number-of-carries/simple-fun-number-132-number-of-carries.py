import itertools
def number_of_carries(a,b):
    return sum(1 for i in itertools.zip_longest( str(a)[::-1] , str(b)[::-1], str(a+b)[::-1], fillvalue='0') if ( int(i[0]) + int(i[1]) )%10 != int(i[2]))