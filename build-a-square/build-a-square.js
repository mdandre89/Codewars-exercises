function generateShape(n){
var r = new Array(n+1).join("+")
var t = []
for(var i=0;i<n;i++){t.push(r)}
return t.join("\n")
}