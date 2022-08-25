function squareOrSquareRoot(array) {
  var vd = [];
  
  for(var i=0; i<array.length; i++){
  if(Math.sqrt(array[i])%1 == 0){vd[i] = Math.sqrt(array[i]); }
  else {vd[i] = array[i]*array[i];}}
  return vd;  
}