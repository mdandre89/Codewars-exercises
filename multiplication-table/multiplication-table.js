multiplicationTable = function(size) {
  var ar  = new Array(size).fill(0)
  return new Array(size).fill(0).map((a,j)=>ar.map((a,i)=>(i+1)*(j+1)))
  
}