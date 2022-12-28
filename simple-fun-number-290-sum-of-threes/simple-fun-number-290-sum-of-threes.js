function sumOfThrees(n) {
  let m  = n.toString(3)
  return /^[10]+$/.test(m) ? m.split("").reduce((a,b,i)=>b!=="0"?`${a}+${3}^${m.length-i-1}`: a,"").replace(/^\+/,"")  : "Impossible"
}