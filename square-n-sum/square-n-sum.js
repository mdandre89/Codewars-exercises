function squareSum(numbers){
console.log(numbers)
return numbers !="" ? numbers.reduce((a,b)=> a+b*b,0):0
}