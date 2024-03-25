function high(x){
var s = x.split(" ").map(i=>i.toLowerCase().split("").map(i=>i.charCodeAt(0)-96).reduce((a,b)=>a+b,0))
return x.split(" ")[s.indexOf(Math.max(...s))]
}