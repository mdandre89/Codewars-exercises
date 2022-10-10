function cubeOdd(arr) {
var res = arr.reduce((a,b)=>Math.abs(b)%2!=0?a+Math.pow(b,3):a,0);
return isNaN(res)?undefined:res
}