# Interlace an arbitrary Number of Strings

 - URL:[https://www.codewars.com/kata/5836ebe4f7e1c56e1a000033](https://www.codewars.com/kata/5836ebe4f7e1c56e1a000033)
 - Id: 5836ebe4f7e1c56e1a000033
 - Language: python
 - Completed on: 2018-02-08T09:00:40.360Z
 - Tags: Fundamentals
 - Description:
Write a function that takes an arbitrary number of strings and interlaces them (combines them by alternating characters from each string).

For example `combineStrings('abc', '123')` should return `'a1b2c3'`.

If the strings are different lengths the function should interlace them until each string runs out, continuing to add characters from the remaining strings.

For example `combineStrings('abcd', '123')` should return `'a1b2c3d'`.

The function should take any number of arguments and combine them.

For example `combineStrings('abc', '123', '£$%')` should return `'a1£b2$c3%'`.

**Note: if only one argument is passed return only that string. If no arguments are passed return an empty string.**
