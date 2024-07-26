function valAndUnits(s) {
var unit = (/[A-Za-z%!?]/gi).test(s)?s.match(/[A-Za-z%!?]/gi).join(""):""
var value = parseFloat(s)
return {val: value, units: unit }
}