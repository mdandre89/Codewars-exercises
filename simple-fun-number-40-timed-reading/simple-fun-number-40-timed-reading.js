function timedReading(maxLength, text) {
  text=text.replace(/[^A-Za-z0-9_]/g," ");
  var t = text.split(" ");
  var s = t.filter(function(m){if(m.length<=maxLength){return m;}})
  return s.length;
}