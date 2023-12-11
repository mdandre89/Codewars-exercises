function ipToInt32(ip){
  return ip.split(".").reverse().reduce((a,b,i)=>a+b*Math.pow(2,8*i),0)
}