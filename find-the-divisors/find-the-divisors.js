function divisors(n) {
var t=[]
  for(var i=2; i<n/2+1;i++){if(n%i==0){t.push(i)} }
  return t!=""? t :n +" is prime"
};