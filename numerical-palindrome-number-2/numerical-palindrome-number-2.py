def palindrome(num):
    if not isinstance(num,int) or num<0:
        return "Not valid"
    num = str(num)
    for i in range(1,len(num)):
        for j in range(0,i+1):
            if pali(num[j:i+1]):
                return True
    return False
    
def pali(s):
    if s==s[::-1] and len(s)>1:
        return True
    return False