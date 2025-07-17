function pattern(n){
var t = []
for(var i=1;i<n+1;i++){
t.push( Array(n-i+1).join(" ") + ls(i) + Array(n-i+1).join(" "))
}
return t.join("\n")
}
function ls(k){
    var s = []
    for(var j =1;j<k;j++){
    s.push(String(j%10))}
    return s.join("") + String(k%10) + s.reverse().join("")}