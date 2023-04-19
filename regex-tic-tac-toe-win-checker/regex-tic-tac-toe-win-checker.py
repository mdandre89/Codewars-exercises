import re
def regex_tic_tac_toe_win_checker(b):
    b1 = ''.join([ b[i:i+3]+'&' for i in range(0,9,3)])
    s = ''.join((''.join(i)+'&' for i in zip(*[ b[i:i+3] for i in range(0,9,3)])))
    if re.search(r'X{3}&|O{3}&',b1) or b[0]==b[4]==b[8]!='-' or b[2]==b[4]==b[6]!='-':
        return True
    if re.search(r'X{3}&|O{3}&',s):
        return True  
    return False