function wordsToHex(words) {
  return words.split(" ").map(a=>"#"+transfo(a))
}

function transfo(i){
var r = i.split("").slice(0,3).map(a=>a.charCodeAt(0).toString(16).toString()).join("")
return r.length>=6? r: r+Array(6+1-r.length).join("0")
}