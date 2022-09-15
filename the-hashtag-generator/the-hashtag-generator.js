function generateHashtag (st) {
  if(st==""){return false}
  var st = st.trim().split(" ").map(a=>a[0].toUpperCase() + a.slice(1)).join("")
  return st.length<=140 ? "#" + st : false
}