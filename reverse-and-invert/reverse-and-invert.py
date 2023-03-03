def reverse_invert(lst):
    print(lst)
    def test(s):
        try: 
            if str(s).count(".")!=0:
                return False
            if int(s) or s==0:
                return True
            return False 
        except:
            return False      
    t = []
    for x in lst:
        if test(x) and x>=0:
            t.append(-int(str(x)[::-1]))
        elif test(x):
            t.append(int(str(-x)[::-1]))
        else:
            pass            
    return t