const mirror = obj => {
var t = {}
for(var key in obj){
if(obj[key]==undefined){t[key]=key.split("").reverse().join("")}
else(t[key]=obj[key])}
return t
};