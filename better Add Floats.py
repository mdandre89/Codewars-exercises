function add(){
var args = Array.prototype.slice.call(arguments);
return args.reduce((s,a)=> add2(s,a));}

function add2(a,b){
var a = a.toString();
var b = b.toString();
if((a.match(/\./g)||[]).length>=2 || (b.match(/\./g)||[]).length>=2){return NaN}
if(a.indexOf(".")!=-1){var a1 = a.split(".")[0]; a2 = a.split(".")[1]}else{var a1 = a; var a2 = ""}
if(b.indexOf(".")!=-1){var b1 = b.split(".")[0]; b2 = b.split(".")[1]}else{var b1 = b; var b2 = ""}
var m = Math.max(a2.length,b2.length);
if(a2.length>=b2.length){var d = a2.length-b2.length;var s = sumStrings(a1+a2,b1+b2+Array(d+1).join("0"));}else{
var d = b2.length-a2.length; var s = sumStrings(a1+a2+Array(d+1).join("0"),b1+b2);}
return m>0 ? ((s.slice(0,s.length-m)||"0")+"."+s.slice(-m)).replace(/0+$/g,"") : s
}

function sumStrings(a,b) { 
var a = a.split("").reverse().join("")
var b = b.split("").reverse().join("")
var s = ""
var r = 0
for(var i=0; i< Math.max(a.length,b.length)+1;i+=1){
  var m = parseInt(a[i]||0) + parseInt(b[i]||0) + r;
  r = Math.floor(m/10);
  s += (m%10).toString()}
return s.split("").reverse().join("").replace(/^0+/, '');}
