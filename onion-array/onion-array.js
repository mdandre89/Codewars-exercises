function isOnionArray(b){
  return b.slice(0,Math.floor(b.length/2)).filter((a,i)=>a+b[b.length-1-i]<=10).length == b.slice(0,Math.floor(b.length/2)).length
}