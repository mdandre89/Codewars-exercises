function climb(n){
  var t = [n];  
  while(n!=1){ 
  if(n%2==0){
  n = n/2;
  t.push(n);}
  else{n = (n-1)/2;
  t.push(n);}
  }
  return t.reverse();
}