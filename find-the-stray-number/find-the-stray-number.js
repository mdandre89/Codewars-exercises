function stray(numbers) {
  var n = numbers.filter(a=> a!=numbers[0])
  return n.length>1?numbers[0]:n[0]
}