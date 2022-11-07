import re
def string_breakers(n, st): 
    new_st = re.sub(r'[ ]+', '', st)
    return '\n'.join(new_st[i:i+n] for i in range(0, len(new_st), n))