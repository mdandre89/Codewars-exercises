function danspower(num, power) {
  return Math.pow(num,power)%2==0?Math.pow(num,power):Math.round(Math.pow(num,power)/10)*10;
}