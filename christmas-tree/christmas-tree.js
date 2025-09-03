function christmasTree(n) {
var t = []
for(var i = 1; i<=n; i++){
t.push(new Array((2*n-2*i+2)/2).join(" ")+new Array(2*i).join("*")+new Array((2*n-2*i+2)/2).join(" "))
}
return t.join("\n")
}