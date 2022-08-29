function scoreThrows(radiuses){
  var s = radiuses.reduce((a,b)=>a+scora(b),0)
  return s!=10*radiuses.length || s==0 ? s:s+100
}


function scora(p){
    if(p > 10){return 0}
    return p < 5? 10 :5}