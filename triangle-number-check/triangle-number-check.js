function isTriangleNumber(t) {
  return typeof t =="number" && Number.isInteger(Math.sqrt(8*t+1)) ? true:false
}