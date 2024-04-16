Array.prototype.except = function(keys)
{ var s = []
if(typeof keys=="number"){keys=[keys]}
for (var i = 0; i<this.length; i++){
if(keys.indexOf(i)==-1){s.push(this[i])}}
return s
}