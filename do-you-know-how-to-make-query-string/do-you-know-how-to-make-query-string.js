function toQueryString (obj) {
var s =""
for(var prop in obj){
if(typeof obj[prop]=="object"){
obj[prop].forEach(a=> s+=prop+"="+a+"&")}
else{s+=prop+"="+obj[prop]+"&"}}
return s.substr(0,s.length-1)
}