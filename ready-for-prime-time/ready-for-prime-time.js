function prime(num) {
  var t = [] 
  for(var i=2; i<=num; i++){if(isprime(i)){t.push(i)}}
  return t
}


function isprime(n){
if(n<=3){return true}
for(var j=2; j<=Math.sqrt(n)+1; j++){if(n%j==0){return false}}
return true
}