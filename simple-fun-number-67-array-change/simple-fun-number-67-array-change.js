function arrayChange(arr) {
  var s=0;
  
  for(var i=0;i<arr.length-1; i++){
  if(arr[i+1]<=arr[i]){
  s+= arr[i]-arr[i+1]+1;
  arr[i+1]=arr[i]+1;}
  }
  return s;
}