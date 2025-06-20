function wordsToObject(input) {
   return  "["+input.match(/[^ ]+ [^ ]+/gi).map(a=>"{name"+" : "+"'"+a.split(" ")[0]+"'"+", id : "+"'"+a.split(" ")[1]+"'}").join(", ")+"]"
}