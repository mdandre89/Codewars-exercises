def palindrome(num):
    if isinstance(num,str) or num<0:
        return 'Not valid'
    num = str(num)
    l = len(num) 
    return num[0:l//2]==num[l//2:][::-1] if l%2==0 else num[0:l//2]==num[l//2+1:][::-1]