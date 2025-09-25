function calculateHypotenuse(a,b){
  if (typeof a =="number" && typeof b =="number"&& a>0&&b>0){
  return parseFloat((Math.sqrt(Math.pow(a,2)+Math.pow(b,2))).toFixed(3))
  }
   throw "error" 
}