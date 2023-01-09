function countNumber(n, x) {
var t=[];
for(var i=0; i<n+1;i++){
if(x%i==0 && x/i<=n){t.push(i)}
}
return t.length
}