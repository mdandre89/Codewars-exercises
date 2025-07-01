import re
def count_smileys(arr):
    t = 0
    for i in arr:
        if re.match(r"(:|;)(-|~)?(\)|D)", i):
            t +=1      
    return t