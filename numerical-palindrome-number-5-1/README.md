# Numerical Palindrome #5 

 - URL:[https://www.codewars.com/kata/58e26b5d92d04c7a4f00020a](https://www.codewars.com/kata/58e26b5d92d04c7a4f00020a)
 - Id: 58e26b5d92d04c7a4f00020a
 - Language: javascript
 - Completed on: 2017-08-31T16:10:56.012Z
 - Tags: Fundamentals
 - Description:
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are: 

* 232
* 110011
* 54322345

Complete the function to test if the given number (`num`) **can be <u>rearranged</u>** to form a numerical palindrome or not. Return a boolean (`true` if it can be rearranged to a palindrome, and `false` if it cannot). Return `"Not valid"` if the input is not an integer or is less than 0.

For this kata, single digit numbers are **NOT** considered numerical palindromes.  


## Examples

```
5        =>  false
2121     =>  true
1331     =>  true 
3357665  =>  true 
1294     =>  false 
"109982" =>  "Not valid"
-42      =>  "Not valid"
```

~~~if:cobol
In COBOL, `num` will always be an integer. Assign `0` to result if `num` is negative or if its digits cannot be rearranged to a palindrome, otherwise `1`.
~~~

## Other Kata in this Series:
<a href="https://www.codewars.com/kata/58ba6fece3614ba7c200017f">Numerical Palindrome #1</a>
<br><a href="https://www.codewars.com/kata/numerical-palindrome-number-1-dot-5">Numerical Palindrome #1.5</a>
<br><a href="https://www.codewars.com/kata/58de819eb76cf778fe00005c">Numerical Palindrome #2</a>
<br><a href="https://www.codewars.com/kata/58df62fe95923f7a7f0000cc">Numerical Palindrome #3</a>
<br><a href="https://www.codewars.com/kata/58e2708f9bd67fee17000080">Numerical Palindrome #3.5</a>
<br><a href="https://www.codewars.com/kata/58df8b4d010a9456140000c7">Numerical Palindrome #4</a>
<br><b>Numerical Palindrome #5</b>

