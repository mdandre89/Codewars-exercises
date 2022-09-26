import re
def split_odd_and_even(n):
    return list(map(int,re.findall(r"[2,4,6,8]+|[1,3,5,7,9]+",str(n))))