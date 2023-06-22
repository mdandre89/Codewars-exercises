# Numerical Palindrome #1.5

 - URL:[https://www.codewars.com/kata/58e09234ca6895c7b300008c](https://www.codewars.com/kata/58e09234ca6895c7b300008c)
 - Id: 58e09234ca6895c7b300008c
 - Language: javascript
 - Completed on: 2017-04-06T16:41:12.672Z
 - Tags: Arrays,Fundamentals
 - Description:
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are:

2332 
<br>110011 
<br>54322345

You'll be given 2 numbers as arguments: ```(num,s)```.  Write a function which returns an array of ```s``` number of numerical palindromes that come after ```num```. If ```num``` is a palindrome itself, it should be included in the count. 

Return "Not valid" instead if any one of the inputs is not an integer or is less than 0.

For this kata, single digit numbers will <u>NOT</u> be considered numerical palindromes. 

```
palindrome(6,4) => [11,22,33,44]
palindrome(59,3) => [66,77,88]
palindrome(101,2) => [101,111]
palindrome("15651",5) => "Not valid" 
palindrome(1221,"8") => "Not valid" 
```

~~~if:haskell
In Haskell, the return type is a Maybe which returns Nothing if either of the inputs is negative."
~~~
~~~if:cobol 
In COBOL, `num` and `s` will always be an integer. Return an empty table if `num` is negative.
~~~

<h2><u>Other Kata in this Series:</u></h2> 
<a href="https://www.codewars.com/kata/58ba6fece3614ba7c200017f">Numerical Palindrome #1</a>
<br><b>Numerical Palindrome #1.5 </b>
<br><a href="https://www.codewars.com/kata/58de819eb76cf778fe00005c">Numerical Palindrome #2</a>
<br><a href="https://www.codewars.com/kata/58df62fe95923f7a7f0000cc">Numerical Palindrome #3</a>
<br><a href="https://www.codewars.com/kata/58e2708f9bd67fee17000080">Numerical Palindrome #3.5</a>
<br><a href="https://www.codewars.com/kata/58df8b4d010a9456140000c7">Numerical Palindrome #4</a>
<br><a href="https://www.codewars.com/kata/58e26b5d92d04c7a4f00020a">Numerical Palindrome #5</a>
