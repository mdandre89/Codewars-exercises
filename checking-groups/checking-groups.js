function groupCheck(s){
var l = s.length;
var i=0
while(i<l){
s=s.replace("()","")
s=s.replace("[]","")
s=s.replace("{}","")
i++;
}
console.log(s,s.length);
return s.length==0? "That group was matched correctly":false;
}