function stringTask(s){
  return /[^aeiouy]/gi.test(s)?s.match(/[^aeiouy]/gi).map(i=>"."+i.toLowerCase()).join(""):""
}