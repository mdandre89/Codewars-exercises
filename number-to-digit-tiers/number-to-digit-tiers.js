function createArrayOfTiers(num) {
var num = num.toString()
var t =[]
for(var i=1;i<=num.length;i++){
t.push(num.substring(0,i))
}
return t
}