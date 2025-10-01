function solution(strng) {
    var t="";
    for(var i=0; i<strng.length;i++){
    if(strng[i] == strng[i].toLowerCase()){t+=strng[i]}else{t+= " " +strng[i]}
    
    }
    return t;
}