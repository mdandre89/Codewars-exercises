function tacofy(word) {
  dictio = {"t":"tomato","l":"lettuce", "c" :"cheese","g":"guacamole","s":"salsa"}
  var t = word.toLowerCase().match(/[tlcgsaeiou]/g,"")||[]
  return  ['shell'].concat(t.map(i=>"aeiou".indexOf(i)!=-1 ? "beef":dictio[i])).concat(["shell"])
  
}