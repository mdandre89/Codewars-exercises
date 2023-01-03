function plantDoubling(n) {
return parseInt(n.toString(2).split("").reduce(function(a,b){return parseInt(a)+parseInt(b)}))
}