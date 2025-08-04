var whatTimeIsIt = function(angle) {
  if(angle<30){return "12:"+("00"+Math.floor(angle%30*2)).slice(-2)}
  return ("00"+Math.floor(angle/30)).slice(-2)+":"+("00"+Math.floor(angle%30*2)).slice(-2);
}