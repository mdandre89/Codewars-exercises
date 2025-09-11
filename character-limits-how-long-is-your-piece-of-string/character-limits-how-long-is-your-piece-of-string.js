function charCheck(text, max, spaces){
if(spaces){
if(text.length<=max){return [true, text]}else{
return [false, text.substr(0,max)]}
}
else{
if(text.replace(/ /g,'').length<=max){return [true, text.replace(/ /g,'')]}
else{
return [false, text.replace(/ /g,'').substr(0,max)]}}};