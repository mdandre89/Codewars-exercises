function alienLanguage(str){
str = str.split(" ");
for (var i=0; i<str.length; i++){
str[i]= str[i].slice(0,str[i].length-1).toUpperCase() + str[i].slice(-1).toLowerCase()
}
  return str.join(" ")
}