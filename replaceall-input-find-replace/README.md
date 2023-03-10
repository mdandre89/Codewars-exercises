# replaceAll(input, find, replace)

 - URL:[https://www.codewars.com/kata/52aaf51822e82a808100066b](https://www.codewars.com/kata/52aaf51822e82a808100066b)
 - Id: 52aaf51822e82a808100066b
 - Language: javascript
 - Completed on: 2022-06-11T13:17:05.897Z
 - Tags: Strings,Regular Expressions,Algorithms
 - Description:
Isn't it annoying how `"string".replace("find", "replace");` only replaces the first match of the `find` string? Write a function, `replaceAll(input, find, replace);` that will replace all matches of the given `find` string with the given `replace` string.

The function will always be called with three strings, so don't worry about validating the arguments.

As with the original `"string".replace(find, replace)`, if `find` is an empty string, it should match _in-between_ each character, effectively inserting `replace` in-between each character, including the start and end of the string. I've given you some tests for this to make it a little clearer.
