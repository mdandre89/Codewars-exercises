function digital_root(n) {
var n = n.toString()
if(n.length==1){return parseInt(n)}
while(n.length>=1){
return digital_root(n.split("").reduce( function(a,b){return parseInt(a)+parseInt(b) } ) ) }
}