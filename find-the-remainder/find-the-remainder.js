function remainder(a, b){
  if (b==0){return 'Divide by zero should return NaN'}
  return b>a ? b%a : a % b
}