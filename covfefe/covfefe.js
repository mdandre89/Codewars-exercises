function covfefe(str){
  var s = str.replace(/coverage/g,"covfefe")
  return str.indexOf("coverage")!=-1?s:s+" covfefe" 
}