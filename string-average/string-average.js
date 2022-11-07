function averageString(s) {
  var dictio = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
  var res = swap(dictio)[Math.floor(s.split(' ').reduce((a,b)=>a+dictio[b],0)/s.split(' ').length)]
  return s==''|| res==undefined?"n/a":res
}

function swap(json){
  var ret = {};
  for(var key in json){
    ret[json[key]] = key;
  }
  return ret;
}