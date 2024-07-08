var findMissing = function (ls) {  
let s = ls.reduce((a,b)=>a+b,0)
let l = ls.length
let q = (ls[ls.length-1] - ls[0])/l
  return ls[0]*(l+1) +q*(l*(l+1)/2) - s
}