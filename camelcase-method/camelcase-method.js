String.prototype.camelCase=function(){
return this!="" ?this.trim().split(" ").map(x=> x[0].toUpperCase() + x.slice(1)).join(""):""
}