def solution(number):
    n = number//3 if number%3!=0 else number//3 -1 
    m = number//5 if number%5!=0 else number//5 -1 
    k = number//15 if number%15!=0 else number//15 -1 
    return 3*n*(n+1)/2 + 5*m*(m+1)/2 - 15*k*(k+1)/2