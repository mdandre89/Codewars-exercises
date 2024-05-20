const generate = length => {
var t =""
for(var i=0;i<length;i++){
t+=(Math.floor(Math.random(0,1)*2)).toString()
}
return t}