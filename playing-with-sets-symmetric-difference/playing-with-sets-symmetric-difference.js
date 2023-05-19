function symDiff(s1, s2){
  var l = new Set(Array.from(s1))
  for(let item of s2){
  l.add(item)
  }
  return new Set(Array.from(l).filter(i=>!(s1.has(i)&&s2.has(i))))
}