function nextPrime(n){
  var i = n + 1
while(!isPrime(i)){i++}
return n>=2 ? i : 2 
}


function isPrime(m){
for(var i = 2; i <= Math.sqrt(m); i++){
if(m%i == 0){return false;}}
return true;
}