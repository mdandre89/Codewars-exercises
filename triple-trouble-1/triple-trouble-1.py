import re
def triple_double(num1, num2):
    return len( set(re.findall(r'(\w)\1{2}', str(num1))).intersection(set(re.findall(r'(\w)\1{1}', str(num2)))) ) >=1