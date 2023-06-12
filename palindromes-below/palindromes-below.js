Number.prototype.palindromeBelow = function(base){
return new Array(this+1).fill(1).map((a,i)=>i).slice(1).filter(a=>a.toString(base)==a.toString(base).split("").reverse().join(""))
}