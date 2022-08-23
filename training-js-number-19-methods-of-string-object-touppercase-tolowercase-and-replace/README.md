# Training JS #19: Methods of String object--toUpperCase() toLowerCase() and replace()

 - URL:[https://www.codewars.com/kata/5728203b7fc662a4c4000ef3](https://www.codewars.com/kata/5728203b7fc662a4c4000ef3)
 - Id: 5728203b7fc662a4c4000ef3
 - Language: javascript
 - Completed on: 2017-03-28T18:32:03.129Z
 - Tags: Fundamentals,Basic Language Features,Language Features,Tutorials
 - Description:
This time we learn three string methods used to change the contents of the string:```toUpperCase()``` ```toLowerCase()``` and ```replace()```.  Their usage:

```javascript
stringObject.toUpperCase()
stringObject.toLowerCase()
stringObject.replace(substring/regexp,replacement)
```
```toUpperCase()``` and ```toLowerCase()``` usage is very simple. No parameters needs accept. It can convert all the characters in the string to uppercase or lowercase. like this:
```javascript
var str="My name is John";
console.log(str.toUpperCase());
console.log(str.toLowerCase());
//output:
MY NAME IS JOHN
my name is john
```
The following is a classic usage. Capitalize the first letter of a sentence:
```javascript
var str="this is an example.";
var result=str[0].toUpperCase()+str.slice(1);
console.log(result);

//output:
This is an example.
```
The example below is to capitalize the first letter of all the words in the sentence. We used the ```split()``` and ```join()``` that we learned last time. 

```javascript
var str="this is an example.";
var words=str.split(" ");
for (var i=0;i<words.length;i++){
  words[i]=words[i][0].toUpperCase()+words[i].slice(1);
}
console.log(words.join(" "));

//output:
This Is An Example.
```

It seems a bit complicated. Let's learn new method to improve it.

```replace()``` can replace the text specified(parameter 1) in the string with parameter 2. For example:
```javascript
var str="this is an example.";
var result=str.replace("this","that");
console.log(result);

//output:
that is an example.
```
Let's use replace() to improve the example above (capitalized the first letter):
```javascript
var str="this is an example.";
var words=str.split(" ");
for (var i=0;i<words.length;i++){
  words[i]=words[i].replace(words[i][0],words[i][0].toUpperCase());
}
console.log(words.join(" "));

//output:
This Is An Example.
```

If the parameter 1 of ```replace()``` is a regular expression, it will be more simple(We don't even need to split the string):

```javascript
var str="this is an example.";
var result=str.replace(/\b\w/g,x=>x.toUpperCase());
console.log(result);

//output:
This Is An Example.
```
This code uses a regular expression and an arrow function. This allows us to achieve a more powerful role in the code. All of these will be learning in the future lesson. We need to do now is to learn the basics.

Another point needs to pay attention: If ```replace()``` uses a regular expression as parameter 1, and all the characters that match the regular expression are replaced(The regular expression uses a global matching option g). If we use a string as a parameter 1, only the first match(from left to right) of the string is replaced. like this:
```javascript
var str="example";
var result=str.replace("e","@");
console.log(result);

//output:
@xample
```
As you can see, the second "e" will not be replaced.


Ok, lesson is over. let's us do some task.

## Task

Coding in function ```alienLanguage```, function accept 1 parameter:```str```. ```str``` is a sentence.

We translate the sentence into an alien language according to the following rules:

Each word in the sentence is separated by spaces. The last letter of each word in the sentence turns to lowercase, and the other letters are capitalized. Looks very strange? Because this is the form of alien language ;-)

for example:

```
alienLanguage("My name is John") should return "My NAMe Is JOHn"
alienLanguage("this is an example") should return "THIs Is An EXAMPLe"
alienLanguage("Hello World") should return "HELLo WORLd"
```
A small hint: The first conversion of the entire string will make the code easier
    
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
 
