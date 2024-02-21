function getLosAngelesPoints(results) { 
  var s = /^Los Angeles [A-Z][a-z]*/i;
  var b = results.filter(a=>s.exec(a[0])).reduce((a,e) => a + Number(e[1].split(':')[0]),0)
  return b
}