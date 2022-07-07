function abbreviate(strng) {
var stri = strng.match(/[\w]+|[^A-Za-z0-9]+/g);
var s ="";
for(var i=0; i<stri.length; i++){
if(stri[i].length>3){s+= stri[i][0] +parseFloat(stri[i].length-2)+ stri[i][stri[i].length-1]; }else{s += stri[i];}
}
return s
}