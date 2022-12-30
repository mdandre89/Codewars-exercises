function arrayCenter(a) {
var mini = Math.min.apply(null, a)
var aver = a.reduce((a, b)=> a + b)/a.length;
return a.filter(i=> Math.abs(i - aver)<mini)
}