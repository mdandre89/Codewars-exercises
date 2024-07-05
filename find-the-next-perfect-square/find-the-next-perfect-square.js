function findNextSquare(sq) {
var t = Math.sqrt(sq)+1
return Number.isInteger(t) ? t*t: -1
}