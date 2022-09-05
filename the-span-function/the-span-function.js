function span(arr, predicate) {
  let ar = arr.map(item => predicate(item)).indexOf(false)
  return ar > -1 ? [arr.slice(0, ar), arr.slice(ar, arr.length)] : [arr, []]
}