function dashatize(num) {
  if(isNaN(num)){return "NaN"}
  if(num<=0){num = -num}
  num = num.toString().split("").map(a=>a%2==0?a:"-"+a+"-").join("").replace(/--/g,"-")
  if(num[0]=="-"){num = num.slice(1)}
  if (num[num.length-1]=="-"){return num.substring(0, num.length - 1);}
  return num
};