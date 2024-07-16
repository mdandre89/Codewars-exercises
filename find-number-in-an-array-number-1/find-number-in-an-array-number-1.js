function duplicateOrUnique(arr){
  var l = arr.length-1
  var n = l*(l+1)/2
  var s = 0;
  for (var i=arr.length; i--;){s+=arr[i];}
  if(arr.length%2==0){return s-n}
  return s-n > 0 ? s-n : n/2 + (5*l+8)/4 - s
}