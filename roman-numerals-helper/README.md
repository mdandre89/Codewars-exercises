# Roman Numerals Helper

 - URL:[https://www.codewars.com/kata/51b66044bce5799a7f000003](https://www.codewars.com/kata/51b66044bce5799a7f000003)
 - Id: 51b66044bce5799a7f000003
 - Language: javascript
 - Completed on: 2017-04-11T15:21:18.079Z
 - Tags: Algorithms
 - Description:
Create a RomanNumerals class that can convert a roman numeral to and from an integer value.  It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method. 

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : `1 <= n < 4000`

In this kata `4` should be represented as `IV`, NOT as `IIII` (the "watchmaker's four").
 

### Examples

```javascript
RomanNumerals.toRoman(1000); // should return 'M'
RomanNumerals.fromRoman('M'); // should return 1000
```
```coffeescript
RomanNumerals.toRoman(1000) # should return 'M'
RomanNumerals.fromRoman('M') # should return 1000
```
```ruby
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
```
```python
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
```
```c
to_roman(1000) // should return 'M'
from_roman('M') // should return 1000
```
```c++
RomanNumerals.to_roman(1000) // should return 'M'
RomanNumerals.from_roman('M') // should return 1000
```
```cobol
      ToRoman(1000)  => result = 'M'
      FromRoman('M') => result = 1000
```
```c#
RomanNumerals.ToRoman(1000) // should return 'M'
RomanNumerals.FromRoman('M') // should return 1000
```
```f#
ToRoman 1000 // should return 'M'
FromRoman "M" // should return 1000
```
```java
RomanNumerals.toRoman(1000) // should return 'M'
RomanNumerals.fromRoman("M") // should return 1000
```
```julia
RomanNumerals.toroman(1000) # should return "M"
RomanNumerals.fromroman("M") # should return 1000
```

### Help

| Symbol | Value |
|-------:|:------|
| I	  |  1    |
| IV  |  4    |
| V	  |  5    |
| X	  |  10   |
| L	  |  50   |
| C	  |  100  |
| D	  |  500  |
| M	  |  1000 |

