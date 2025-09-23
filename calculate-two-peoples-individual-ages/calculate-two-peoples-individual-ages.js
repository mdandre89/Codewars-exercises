function getAges(s,d){
var x = (s+d)/2
var y = s - (s+d)/2
return s*d<0||x*y<0? null: [x,y]
};