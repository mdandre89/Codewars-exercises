function vowel2index(str) {
return str.split("").map((a,ind)=>"aeiouAEIOU".indexOf(a)!=-1? ind+1:a).join("")
}