function parseF(s) {
console.log(s);
if (isNaN(s) || s===true || s===false || s===undefined){ return null;} else{ return Number(s);}
}