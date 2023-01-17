function rangeBitCount(a, b) {
var tot=0;
for(var i = a; i<=b;i++){
if(i.toString(2).match(/1/g)!=null){
tot += i.toString(2).match(/1/g).length;}
}
  return tot
}