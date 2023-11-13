function getExponent(n,p){
var i=1
if(p<=1){return null}
while(n%Math.pow(p,i)==0){i++}
return i-1
}