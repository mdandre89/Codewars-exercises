import re
def inside_out(s):
    return re.sub(r"(\w+)",lambda y : update(y.group()),s)
    

def update(x):
    len_substi = len(x)
    if len_substi <4: return x 
    if len_substi % 2 == 0:
        return x[:len_substi//2][::-1] + x[len_substi//2:][::-1]
    return x[:len_substi//2][::-1] + x[len_substi//2] + x[len_substi//2+1:][::-1] 