function getConsectiveItems(items, key){
var s = new RegExp(key.toString()+"*", 'g')
return items.toString().match(s).reduce((a,b)=>a.length>b.length?a:b).length
}