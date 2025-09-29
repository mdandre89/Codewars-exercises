function towerBuilder(n) {
var t =[]
for(var i=1; i<=n; i++){
t.push(new Array(n-i+1).join(' ') + new Array(2*i).join('*')+ new Array(n-i+1).join(' '))
}
return n>1? t :  ['*']
}