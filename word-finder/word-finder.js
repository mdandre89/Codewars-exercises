function Dictionary(words) {
  this.words = words;
}

Dictionary.prototype.getMatchingWords = function(pattern) {
  return this.words.filter(word=>word.match(new RegExp("^" + pattern.replace(new RegExp(/\?{1}/gm) , "\\w{1}") + "$", "gm")))
}