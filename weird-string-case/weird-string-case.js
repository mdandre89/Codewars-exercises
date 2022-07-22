function toWeirdCase(strng){
  return strng.split(" ").map(a=>a.split("").map((b,i)=>i%2==0?b.toUpperCase():b.toLowerCase()).join("")).join(" ")
}