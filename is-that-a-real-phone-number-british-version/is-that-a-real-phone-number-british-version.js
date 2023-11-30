function validateNumber(str){
str = str.replace(/-/g,"");
var OK = re = /(^\+447|07\d{9}$)/g.exec(str);
if(OK){return 'In with a chance';}
else{ return 'Plenty more fish in the sea';}
}