function arrayPacking(a) {
return parseInt(a.map(s=>("000000000" + s.toString(2)).substr(-8)).reverse().join(""),2)
}