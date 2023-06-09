function parseHTMLColor(c) {
  if(c[0] != "#"){c = PRESET_COLORS[c.toLowerCase()]}
  if(c.length==7){
  return {r:parseInt(c.substr(1,2),16),g:parseInt(c.substr(3,2),16),b:parseInt(c.substr(5,2),16)}}
  if(c.length==4){return {r:parseInt(c.substr(1,1)+c.substr(1,1),16),g:parseInt(c.substr(2,1)+c.substr(2,1),16),b:parseInt(c.substr(3,1)+c.substr(3,1),16)}}
}