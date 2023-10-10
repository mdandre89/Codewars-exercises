var solution = function(fA, sA) {
  return fA.reduce((a,b,i)=>a+Math.pow(Math.abs(b-sA[i]),2),0)/fA.length
}