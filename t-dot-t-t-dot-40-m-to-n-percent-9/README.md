# T.T.T.40: m to n % 9

 - URL:[https://www.codewars.com/kata/57b2cef5d2a31c3965000a43](https://www.codewars.com/kata/57b2cef5d2a31c3965000a43)
 - Id: 57b2cef5d2a31c3965000a43
 - Language: javascript
 - Completed on: 2022-06-14T15:02:42.135Z
 - Tags: Puzzles,Games
 - Description:
## Description

We have a number sequence that is from `m` to `n`. Please calculate the remainder of the number % 9. 

For example:

```
a number sequence from 1 to 8 is 12345678

12345678 % 9 = 0

so easy, isn't it?

When the number sequence is very very long, 
you should find a better way to calculate it.

a number sequence from 1 to 20 is:
1234567891011121314151617181920

1234567891011121314151617181920 % 9 = ?

```

## Task

Complete function `nMod9()` that accepts two arguments `m` and `n`(two positive integer and m < n). Their meaning please refer to the above explanation.

You should return a number that is the result of number sequence % 9.

## Examples

```javascript
nMod9(1,2) === 3     //12 % 9 = 3
nMod9(1,3) === 6     //123 % 9 = 6
nMod9(2,3) === 5     //23 % 9 = 5
nMod9(1,8) === 0     //12345678 % 9 = 0
nMod9(1,20) === 3    //123456789101112...181920 % 9 = 3
nMod9(1,2016) === 0  //123456789101112...20152016 % 9 = 0
```
