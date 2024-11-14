function reverseByCenter(s){
 var l = s.length;
if(l%2==0){
return s.slice(l/2,l)+s.slice(0,l/2)
}else{
return s.slice(Math.floor(l/2)+1,l) + s[Math.floor(l/2)]+s.slice(0,Math.floor(l/2))
}
}