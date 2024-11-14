function narcissistic( n ) {
  var l = n.toString().length
  return n.toString().split("").map(a=>Math.pow(parseInt(a),l)).reduce((a,b)=>a+b)==n
}