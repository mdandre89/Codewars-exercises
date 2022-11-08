import re
def dup(arr):
    return [re.sub(r"((.)\2*)",lambda x: x.group(2),i) for i in arr]