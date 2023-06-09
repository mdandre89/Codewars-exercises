function wordSearch(query, seq){
var q = new RegExp(".*"+query.toLowerCase()+".*");
var t =  seq.filter(a=> q.test(a.toLowerCase()))
return  t != '' ? t : ["Empty"]
}