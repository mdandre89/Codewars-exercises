def solution(n):
    return [sum(1 for i in range(0,n,3) if i%5!=0), sum(1 for i in range(0,n,5)if i%3!=0),sum(1 for i in range(0,n,15))-1]