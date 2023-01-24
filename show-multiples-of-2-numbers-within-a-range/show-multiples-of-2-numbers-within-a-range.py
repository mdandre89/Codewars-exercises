# Python version: return multiples of 2 numbers in a list
def multiples(s1,s2,s3):
    n =min([j for j in range(max(s1,s2),s1*s2+1) if j%s1==0 and j%s2==0])
    return [n*j for j in range(1,s3) if n*j < s3] 