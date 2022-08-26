function solution(hour) {
  var hours2 = hour.toString()
  if (hours2.length>4 || hours2.length<3){throw "shit"}
  return hours2.substring(0,hours2.length-2) +":"+ hours2.substring(hours2.length-2,hours2.length)
}