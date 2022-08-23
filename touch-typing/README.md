# Touch Typing

 - URL:[https://www.codewars.com/kata/57b9d705f302997e61000157](https://www.codewars.com/kata/57b9d705f302997e61000157)
 - Id: 57b9d705f302997e61000157
 - Language: javascript
 - Completed on: 2018-02-22T11:54:25.980Z
 - Tags: Regular Expressions,Algorithms
 - Description:
In this kata you're given a string which can include English lowercase letters, digits, and spaces. Your task is to write a function which will return a string of 'L' and 'R' chars which displays in which order should the hands be used to type it.

## Rules of touch typing

1. The digits before (including) `5`, letters of the first row before (including) `t`, letters of the second row before (including) `g` and letters of the third row before (including) `b` are typed with left hand, the other digits and numbers are typed with right hand.
1. Space is typed with left hand if the non-space char you typed before was typed with right one, and vice versa. If it is the first char, it's typed with left hand.

_Every string you're given is a correct string which includes only digits, lowercase letters and spaces. Strings need not be validated._

## Examples

`"i love programming"` -> `"RLRRLLRRLRLLLRRRRL"`  
`"  two spaces"` -> `"LLLLRLLRLLLL"`  

#### Good luck!
