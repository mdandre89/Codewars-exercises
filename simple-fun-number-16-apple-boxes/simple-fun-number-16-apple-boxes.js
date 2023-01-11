function appleBoxes(k) {
  var s = 0;
  for(var i=0; i<k; i+=2){
  s = s + -2*i-1;
  }
  if(k%2==0){return s+k*k}
  else{
  return s;}
}