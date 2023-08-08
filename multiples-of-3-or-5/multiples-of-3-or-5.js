function solution(number){
  var x = number%3!=0 ? Math.floor(number/3) : Math.floor(number/3) - 1 
  var y = number%5!=0 ? Math.floor(number/5) : Math.floor(number/5) - 1
  var z = Math.floor(number/15)
  return 3*x*(x+1)/2 +5*y*(y+1)/2 - 15*z*(z+1)/2
}