function isItANum(str) {
str = str.match(/\d/gi)
return str && /^0\d{10}$/.test(str.join(""))? str.join("").match(/^0\d{10}/)[0]: "Not a phone number"
}