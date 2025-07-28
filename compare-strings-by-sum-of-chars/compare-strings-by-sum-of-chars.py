import string 

def compare(s1,s2):
    if  s1==None or any(x not in string.ascii_lowercase for x in s1.lower()):
        print("a")
        s1=""
    
    if s2==None or any(x not in string.ascii_lowercase for x in s2.lower()):
        print("b")
        s2=""
        
    if s1==s2:
        return True
    elif sum([ord(x) for x in s1.upper()]) == sum([ord(y) for y in s2.upper()]):
        return True 
    else:
        return False