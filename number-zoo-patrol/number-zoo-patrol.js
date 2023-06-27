function findNumber(ar) {
  for(var i=1;i<ar.length+1;i++){
  if(ar.indexOf(i)==-1){
  return i}
  }
}