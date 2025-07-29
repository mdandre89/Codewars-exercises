function collatz(n){
  if(n<=1){return "1"}
var t =[]
while(n>1){
t.push(n)
if(n%2==0){n = n/2}
else{n = 3*n+1}}
return t.join("->")+"->1"
}