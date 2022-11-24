def solution(s):
    return [s[i]+s[i+1] for i in range(len(s)) if i%2==0] if len(s)%2==0 else [s[i]+s[i+1] for i in range(len(s)) if i%2==0 and i<len(s)-1] + [s[-1]+"_"]