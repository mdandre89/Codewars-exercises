function calculate(num1,num2){
console.log(num1)
return bin2dec(num1)+bin2dec(num2)
}


function bin2dec(num){
    return num.split('').reverse().reduce(function(x, y, i){
      return (y === '1') ? x + Math.pow(2, i) : x;
    }, 0);
  }