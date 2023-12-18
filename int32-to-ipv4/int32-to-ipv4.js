function int32ToIp(int32){
var t = []
for(var i = 3; i>-1;i--){
var y  = Math.trunc(int32/Math.pow(2,8*i))
t.push(Math.trunc(int32/Math.pow(2,8*i)))
int32 = int32 - y*Math.pow(2,8*i)
}
return t.join('.')
}