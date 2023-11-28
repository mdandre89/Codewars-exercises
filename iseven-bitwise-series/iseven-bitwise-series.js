function isEven(n) { 
  if (n==2){return true}
  if (n==1){return false}
  return !isEven(n-1)
}