function caesarEncode(phrase, shift) {
  return phrase.split(" ").map((a,i)=> cypher(a,shift+i)).join(" ")
}


function cypher(word,k){
var alpha = "abcdefghijklmnopqrstuvwxyz"
return word.split("").map((a,b)=>alpha[(alpha.indexOf(a)+k)%26]).join("")

}