function solution(roman){
    dictio = {"I":1,"V":5,"X":10,"L":50,"C":100,"M":1000,"D":500};
    var t = 0;
    if(roman.indexOf("IV")!=-1){
    roman = roman.replace(/IV/,"")  
    t+=4}
    if(roman.indexOf("XL")!=-1){
    roman = roman.replace(/XL/,"")  
    t+=40}    
    if(roman.indexOf("IX")!=-1){
    roman = roman.replace(/IX/,"")  
    t+=9}     
    if(roman.indexOf("CM")!=-1){
    roman = roman.replace(/CM/,"")  
    t+=900}
    if(roman.indexOf("CD")!=-1){
    roman = roman.replace(/CD/,"")  
    t+=400}
    for(var j=0; j<roman.length;j++){
    t+=dictio[roman[j]]}
    return t}