RomanNumerals = {}

RomanNumerals.fromRoman = function fromRoman(roman){
    var dictio = {"I":1,"V":5,"X":10,"L":50,"C":100,"M":1000,"D":500};
    var t = 0;
    if(roman.indexOf("IV")!=-1){roman = roman.replace(/IV/,"")  
    t+=4}
    if(roman.indexOf("XL")!=-1){roman = roman.replace(/XL/,"")  
    t+=40}    
    if(roman.indexOf("IX")!=-1){roman = roman.replace(/IX/,"")  
    t+=9}     
    if(roman.indexOf("CM")!=-1){roman = roman.replace(/CM/,"")  
    t+=900}
    if(roman.indexOf("CD")!=-1){roman = roman.replace(/CD/,"")  
    t+=400}
    for(var j=0; j<roman.length;j++){t+=dictio[roman[j]]}
    return t}
    
RomanNumerals.toRoman = function toRoman(num){
dictio= {9:"IX", 8:"VIII", 7:"VII", 6: "VI", 5 :"V", 4: "IV", 3:"III", 2:"II", 1:"I", 0:""}
centio = {9:"CM", 8:"DCCC", 7:"DCC", 6: "DC", 5 :"D", 4: "CD", 3:"CCC", 2:"CC", 1:"C", 0:""}
decio = {9:"XC", 8:"LXXX", 7:"LXX", 6: "LX", 5 :"L", 4: "XL", 3:"XXX", 2:"XX", 1:"X", 0:""}
var num = num.toString()
var t =""
if(num/1000>=1){t+=new Array(Math.floor(num/1000)+1).join("M")
num %=1000}
if(num/100>=1){t+=centio[Math.floor(num/100)]
num %=100}
if(num/10>=1){t+=decio[Math.floor(num/10)]
num %=10}
t += dictio[num]
return t
}    