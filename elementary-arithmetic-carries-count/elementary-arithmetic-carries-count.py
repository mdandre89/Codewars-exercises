def solve(input_string):
    return '\n'.join(number_of_carries( int(i.split()[0]), int(i.split()[1])) for i in input_string.split("\n"))
    
import itertools 
def number_of_carries(a,b):
    result = sum(1 for i in itertools.zip_longest( str(a)[::-1] , str(b)[::-1], str(a+b)[::-1], fillvalue='0') if ( int(i[0]) + int(i[1]) )%10 != int(i[2]))
    return 'No carry operation' if result == 0 else str(result) + ' carry operations'