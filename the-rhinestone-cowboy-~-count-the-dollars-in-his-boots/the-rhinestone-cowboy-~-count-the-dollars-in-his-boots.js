function cowboysDollars(boots) {
var botlef = boots[0].substring(0, boots[0].indexOf("&")).match(/\[\(1\)\]/g)
var botrgt = boots[1].substring(0, boots[0].indexOf("&")).match(/\[\(1\)\]/g)
return "This Rhinestone Cowboy has "+[botrgt==null? "0":botrgt.length]+ " dollar bills in his right boot and "+[botlef==null? "0":botlef.length]+" in the left"
}