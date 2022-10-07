function positiveSum(arr) {
  return arr!=""?arr.reduce((a,i)=>i>0?a+i:a,0) :0
}