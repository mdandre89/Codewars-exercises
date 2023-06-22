# Numerical Palindrome #2 

 - URL:[https://www.codewars.com/kata/58de819eb76cf778fe00005c](https://www.codewars.com/kata/58de819eb76cf778fe00005c)
 - Id: 58de819eb76cf778fe00005c
 - Language: python
 - Completed on: 2017-04-11T10:57:37.937Z
 - Tags: Fundamentals
 - Description:
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are: 

<p>2332
<br>110011
<br>54322345

For this kata, single digit numbers will <u>not</u> be considered numerical palindromes. 

For a given number ```num```, write a function to test if the number <b>contains</b> a numerical palindrome or not and return a boolean (true if it does and false if does not). Return "Not valid" if the input is not an integer or is less than 0. 

Note: Palindromes should be found <u>without</u> permutating ```num```. 

```
palindrome(5) => false
palindrome(1221) => true
palindrome(141221001) => true
palindrome(1215) => true 
palindrome(1294) => false 
palindrome("109982") => "Not valid"
```

```haskell

In Haskell, this returns a Maybe Bool, with Nothing for an input less than zero.
```
~~~if:cobol

In COBOL, `num` will always be an integer. Return `1` if it contains a numerical palindrome, otherwise `0`.
~~~

<h2><u>Other Kata in this Series:</u></h2> 
<a href="https://www.codewars.com/kata/58ba6fece3614ba7c200017f">Numerical Palindrome #1</a>
<br><a href="https://www.codewars.com/kata/numerical-palindrome-number-1-dot-5">Numerical Palindrome #1.5</a>
<br><b>Numerical Palindrome #2</b>
<br><a href="https://www.codewars.com/kata/58df62fe95923f7a7f0000cc">Numerical Palindrome #3</a>
<br><a href="https://www.codewars.com/kata/58e2708f9bd67fee17000080">Numerical Palindrome #3.5</a>
<br><a href="https://www.codewars.com/kata/58df8b4d010a9456140000c7">Numerical Palindrome #4</a>
<br><a href="https://www.codewars.com/kata/58e26b5d92d04c7a4f00020a">Numerical Palindrome #5</a>

