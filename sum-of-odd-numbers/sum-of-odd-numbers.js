function rowSumOddNumbers(n) {
  start = 1 + 2*( n*(n-1)/2)
  m = n-1
  return  n*start + 2*(m*(m+1)/2) ; 
}