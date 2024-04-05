function grille(message, code) {
  var s =""
  var cy = code.toString(2).split("").reverse()
   return message.split("").reverse().filter((a,i) =>cy[i]=="1").reverse().join("")
}