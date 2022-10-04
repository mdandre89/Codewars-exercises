import re 
def sum_from_string(string):
    return sum([int(j) for j in re.findall(r'\d+',string)])