function longest(s1, s2) {
var t = (s1+s2).split("");
return t.filter(function(el,ind,ar){if(ar.slice(0,ind).indexOf(el)==-1){return true;}else{false;}}).sort().join("")
}