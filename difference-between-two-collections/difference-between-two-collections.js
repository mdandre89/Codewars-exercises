function diff(a, b){
var s = a.concat(b).filter(i=>!(a.indexOf(i)>=0&&b.indexOf(i)>=0));
return s.filter((item, pos, self)=>self.indexOf(item) == pos).sort();
}