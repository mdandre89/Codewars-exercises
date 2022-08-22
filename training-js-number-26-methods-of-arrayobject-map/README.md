# Training JS #26: methods of arrayObject---map()

 - URL:[https://www.codewars.com/kata/572fdeb4380bb703fc00002c](https://www.codewars.com/kata/572fdeb4380bb703fc00002c)
 - Id: 572fdeb4380bb703fc00002c
 - Language: javascript
 - Completed on: 2017-06-17T16:10:55.837Z
 - Tags: Fundamentals,Basic Language Features,Language Features,Tutorials
 - Description:
This lesson we learn a very useful method of array: ```map()```. The map() method creates a new array with the results of calling a provided function on every element in this array. This method can make people lazy ;-) because it can significantly reduce the amount of code input. For more information, please refer to: [Array.prototype.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

Here are some examples to help us understand the use of ```map()```:

This example calculates the square root of each element:
```javascript
//example1: Direct use of the existing function
var a=[1,4,9,16]
var b=a.map(Math.sqrt)
console.log(a)   //output: [ 1, 4, 9, 16 ]
console.log(b)   //output: [ 1, 2, 3, 4 ]
```
This example increases the value of each element by 1:
```javascript
//example2: Using simple custom functions
var a=[1,2,3,4]
var b=a.map(x=>x+1)
console.log(a)   //output: [ 1, 2, 3, 4 ]
console.log(b)   //output: [ 2, 3, 4, 5 ]
```
This example will take the index of the array as a value:
```javascript
var a=[...Array(4)]
var b=a.map((_,i)=>i)
var c=[...Array(4)].map((_,i)=>i)  
var d=Array.prototype.map.call(a,(_,i)=>i)
console.log(a)   //output: [ undefined, undefined, undefined, undefined ]
console.log(b)   //output: [ 0, 1, 2, 3 ]
console.log(c)   //output: [ 0, 1, 2, 3 ]
console.log(d)   //output: [ 0, 1, 2, 3 ]
```
In this example, a is an initialized array, we can see that the value of all the elements is undefined. b c d is the three different form, using the map() method to assign each element to the index of the element. Need to pay attention to is that this time the map method uses two parameters, the first argument represents the element itself, the second parameter represents the index of elements, we only use the second parameter, but first parameter can not be omitted, so we use the underscore (also with other characters, use the underscore is just to let the reader know this argument is not used).

The following example is the simulation of the reverse method, which uses three parameters, the third parameter represents the array itself:
```javascript
var a=[2,4,6,8]
var b=a.map((_,i,arr)=>arr[arr.length-1-i])
console.log(a)   //output: [ 2, 4, 6, 8 ]
console.log(b)   //output: [ 8, 6, 4, 2 ]
```


Ok, lesson is over. let's us do some task.

## Task

Coding in function ```isolateIt```. function accept 1  parameters ```arr```, it's a string array. Your task is to put a character "|" into the middle of each element. 

If the string length is an even number, use the insert method. for example: ```"abcd"``` should became ```"ab|cd"```. ```"|"``` should be inserted between ```ab``` and ```cd```.

If the string length is an odd number, use the replacement method. for example: ```"abcde"``` should became ```"ab|de"```. Character ```c``` will be replaced by ```|```.

The original array should not be changed, you need to return a new array(if you use the map method, you do not need to worry about this).

## Example

```
isolateIt(["abcd","efgh"]) should return ["ab|cd","ef|gh"]
isolateIt(["abcde","fghij"]) should return ["ab|de","fg|ij"]
isolateIt(["1234","56789"]) should return ["12|34","56|89"]
```

a little hint: Flexible use of ```slice()``` Will make the work more simple.
    
## [Series](http://github.com/myjinxin2015/Katas-list-of-Training-JS-series)

( ↑↑↑ Click the link above can get my newest kata list, Please add it to your favorites)

 - [#1: create your first JS function helloWorld](http://www.codewars.com/kata/571ec274b1c8d4a61c0000c8)
 - [#2: Basic data types--Number](http://www.codewars.com/kata/571edd157e8954bab500032d)
 - [#3:  Basic data types--String](http://www.codewars.com/kata/571edea4b625edcb51000d8e)
 - [#4:  Basic data types--Array](http://www.codewars.com/kata/571effabb625ed9b0600107a)
 - [#5:  Basic data types--Object](http://www.codewars.com/kata/571f1eb77e8954a812000837)
 - [#6:  Basic data types--Boolean and conditional statements if..else](http://www.codewars.com/kata/571f832f07363d295d001ba8)
 - [#7:  if..else and ternary operator](http://www.codewars.com/kata/57202aefe8d6c514300001fd)
 - [#8: Conditional statement--switch](http://www.codewars.com/kata/572059afc2f4612825000d8a)
 - [#9: loop statement --while and do..while](http://www.codewars.com/kata/57216d4bcdd71175d6000560)
 - [#10: loop statement --for](http://www.codewars.com/kata/5721a78c283129e416000999)
 - [#11: loop statement --break,continue](http://www.codewars.com/kata/5721c189cdd71194c1000b9b)
 - [#12: loop statement --for..in and for..of](http://www.codewars.com/kata/5722b3f0bd5583cf44001000)
 - [#13: Number object and  its properties](http://www.codewars.com/kata/5722fd3ab7162a3a4500031f)
 - [#14: Methods of Number object--toString() and toLocaleString()](http://www.codewars.com/kata/57238ceaef9008adc7000603)
 - [#15: Methods of Number object--toFixed(), toExponential() and toPrecision()](http://www.codewars.com/kata/57256064856584bc47000611)
 - [#16: Methods of String object--slice(), substring() and substr()](http://www.codewars.com/kata/57274562c8dcebe77e001012)
 - [#17: Methods of String object--indexOf(), lastIndexOf() and search()](http://www.codewars.com/kata/57277a31e5e51450a4000010)
 - [#18: Methods of String object--concat() split() and its good friend join()](http://www.codewars.com/kata/57280481e8118511f7000ffa)
 - [#19: Methods of String object--toUpperCase() toLowerCase() and replace()](http://www.codewars.com/kata/5728203b7fc662a4c4000ef3)
 - [#20: Methods of String object--charAt() charCodeAt() and fromCharCode()](http://www.codewars.com/kata/57284d23e81185ae6200162a)
 - [#21: Methods of String object--trim() and the string template](http://www.codewars.com/kata/5729b103dd8bac11a900119e)
 - [#22: Unlock new skills--Arrow function,spread operator and deconstruction](http://www.codewars.com/kata/572ab0cfa3af384df7000ff8)
 - [#23: methods of arrayObject---push(), pop(), shift() and unshift()](http://www.codewars.com/kata/572af273a3af3836660014a1)
 - [#24: methods of arrayObject---splice() and slice()](http://www.codewars.com/kata/572cb264362806af46000793)
 - [#25: methods of arrayObject---reverse() and sort()](http://www.codewars.com/kata/572df796914b5ba27c000c90)
 - [#26: methods of arrayObject---map()](http://www.codewars.com/kata/572fdeb4380bb703fc00002c)
 - [#27: methods of arrayObject---filter()](http://www.codewars.com/kata/573023c81add650b84000429)
 - [#28: methods of arrayObject---every() and some()](http://www.codewars.com/kata/57308546bd9f0987c2000d07)
 - [#29: methods of arrayObject---concat() and join()](http://www.codewars.com/kata/5731861d05d14d6f50000626)
 - [#30: methods of arrayObject---reduce() and reduceRight()](http://www.codewars.com/kata/573156709a231dcec9000ee8)
 - [#31: methods of arrayObject---isArray() indexOf() and toString()](http://www.codewars.com/kata/5732b0351eb838d03300101d)
 - [#32: methods of Math---round() ceil() and floor()](http://www.codewars.com/kata/5732d3c9791aafb0e4001236)
 - [#33: methods of Math---max() min() and abs()](http://www.codewars.com/kata/5733d6c2d780e20173000baa)
 - [#34: methods of Math---pow() sqrt() and cbrt()](http://www.codewars.com/kata/5733f948d780e27df6000e33)
 - [#35: methods of Math---log() and its family](http://www.codewars.com/kata/57353de879ccaeb9f8000564)
 - [#36: methods of Math---kata author's lover:random()](http://www.codewars.com/kata/5735956413c2054a680009ec)
 - [#37: Unlock new weapon---RegExp Object](http://www.codewars.com/kata/5735e39313c205fe39001173)
 - [#38: Regular Expression--"^","$", "." and test()](http://www.codewars.com/kata/573975d3ac3eec695b0013e0)
 - [#39: Regular Expression--"?", "*", "+" and "{}"](http://www.codewars.com/kata/573bca07dffc1aa693000139)
 - [#40: Regular Expression--"|", "[]" and "()"](http://www.codewars.com/kata/573d11c48b97c0ad970002d4)
 - [#41: Regular Expression--"\"](http://www.codewars.com/kata/573e6831e3201f6a9b000971)
 - [#42: Regular Expression--(?:), (?=) and (?!)](http://www.codewars.com/kata/573fb9223f9793e485000453)
 
