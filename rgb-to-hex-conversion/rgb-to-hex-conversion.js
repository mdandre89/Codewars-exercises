function rgb(r, g, b){
        console.log(r,g,b)
  var s = [r,g,b].map(a=>Math.max(0,Math.min(255,a))!=0?Math.max(0,Math.min(255,a)).toString(16):"00")
  return s.join("").toUpperCase()
}