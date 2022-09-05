import re
from itertools import zip_longest
def road_kill(photo):
    r = [(i[1],len(i[0])) for i in re.findall(r'(([A-Za-z ])\2*)',photo.replace('=',''))]
    for i in ANIMALS:
        m = [(i[1],len(i[0])) for i in re.findall(r'(([A-Za-z ])\2*)',i)]
        try:
            if all( j[0][0]==j[1][0] and j[0][1]>=j[1][1]  for j in zip_longest(r,m)):
                return i
            if all( j[0][0]==j[1][0] and j[0][1]>=j[1][1]  for j in zip_longest(r,m[::-1])):
                return i 
        except:
            pass
    return '??'