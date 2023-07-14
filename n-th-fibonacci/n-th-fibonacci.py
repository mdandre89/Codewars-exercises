def nth_fib(n):
  i=0
  a = 1
  b = 0
  while i<=n-2:
      temp = a
      a = a + b
      b = temp
      i+=1
  return b