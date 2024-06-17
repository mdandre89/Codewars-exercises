function formatWords(words){
  if(words=="" || words==null){return ""}
  var s = words.filter(a=>a!="")
  return s.length>1?s.slice(0,s.length-1).join(", ")+" and " + s[s.length-1] : s[0]
}