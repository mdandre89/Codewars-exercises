function mixFruit (arr) {
var reg = [ "banana", "orange", "apple", "lemon", "grapes"];
var spec = ["avocado", "strawberry" , "mango"];
var s = arr.reduce((s,i) => reg.concat(spec).includes(i.toLowerCase())?(reg.includes(i.toLowerCase())?s+5:s+7):s+9,0)
return Math.round(s/arr.length)
}