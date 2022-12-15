function ROT135(input) {
return input.split("").map(function(t){return changeChr(t)}).join("")
}

function changeChr(j){
if(j.match(/[a-z]/)){return String.fromCharCode((j.charCodeAt()+13-97)%26 + 97)}
else if(j.match(/[A-Z]/)){return String.fromCharCode((j.charCodeAt()+13-65)%26 + 65)}
else if (j.match(/[0-9]/)){return (parseInt(j)+5)%10}
else{return j}
}