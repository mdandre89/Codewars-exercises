function presses(phrase) {
  var  dictio = {"A":"ABC2","B":"ABC2","C":"ABC2","2":"ABC2","D":"DEF3","E":"DEF3","F":"DEF3","3":"DEF3",
    "1":"1","G":"GHI4","H":"GHI4","I":"GHI4","4":"GHI4","J":"JKL5","K":"JKL5","L":"JKL5","5":"JKL5",
    "M":"MNO6","N":"MNO6","O":"MNO6","6":"MNO6","P":"PQRS7","Q":"PQRS7","R":"PQRS7","S":"PQRS7","7":"PQRS7",
    "T":"TUV8","U":"TUV8","V":"TUV8","8":"TUV8","W":"WXYZ9","X":"WXYZ9","Y":"WXYZ9","Z":"WXYZ9","9":"WXYZ9",
    " ": " 0","0":" 0","*":"*","#":"#"}  
    return phrase.toUpperCase().split("").map(a=>dictio[a].indexOf(a)+1).reduce((a,b)=>a+b)
}