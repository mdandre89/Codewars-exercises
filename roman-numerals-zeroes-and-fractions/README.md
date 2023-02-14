# Roman numerals, Zeroes and Fractions

 - URL:[https://www.codewars.com/kata/55832eda1430b01275000059](https://www.codewars.com/kata/55832eda1430b01275000059)
 - Id: 55832eda1430b01275000059
 - Language: python
 - Completed on: 2017-11-10T14:10:36.471Z
 - Tags: Validation,Algorithms
 - Description:
We all know about Roman Numerals, and if not, here's a nice [introduction kata](http://www.codewars.com/kata/5580d8dc8e4ee9ffcb000050). And if you were anything like me, you 'knew' that the numerals were not used for zeroes or fractions; but not so!

I learned something new today: the [Romans did use fractions](https://en.wikipedia.org/wiki/Roman_numerals#Special_values) and there was even a glyph used to indicate zero.

So in this kata, we will be implementing Roman numerals and fractions.

Although the Romans used base 10 for their counting of units, they used base 12 for their fractions. The system used dots to represent twelfths, and an `S` to represent a half like so:

* <sup>1</sup>/<sub>12</sub> = `.`
* <sup>2</sup>/<sub>12</sub> = `:`
* <sup>3</sup>/<sub>12</sub> = `:.`
* <sup>4</sup>/<sub>12</sub> = `::`
* <sup>5</sup>/<sub>12</sub> = `:.:`
* <sup>6</sup>/<sub>12</sub> = `S`
* <sup>7</sup>/<sub>12</sub> = `S.`
* <sup>8</sup>/<sub>12</sub> = `S:`
* <sup>9</sup>/<sub>12</sub> = `S:.`
* <sup>10</sup>/<sub>12</sub> = `S::`
* <sup>11</sup>/<sub>12</sub> = `S:.:`
* <sup>12</sup>/<sub>12</sub> = `I` (as usual)

Further, zero was represented by `N`


## Kata

Complete the method that takes two parameters: an integer component in the range 0 to 5000 inclusive, and an optional fractional component in the range 0 to 11 inclusive.

You must return a string with the encoded value. Any input values outside the ranges given above should return `"NaR"` (i.e. "Not a Roman" :-)


## Examples

```python
roman_fractions(-12)     #=> "NaR"
roman_fractions(0, -1)   #=> "NaR"
roman_fractions(0, 12)   #=> "NaR"
roman_fractions(0)       #=> "N"
roman_fractions(0, 3)    #=> ":."
roman_fractions(1)       #=> "I"
roman_fractions(1, 0)    #=> "I"
roman_fractions(1, 5)    #=> "I:.:"
roman_fractions(1, 9)    #=> "IS:."
roman_fractions(1632, 2) #=> "MDCXXXII:"
roman_fractions(5000)    #=> "MMMMM"
roman_fractions(5001)    #=> "NaR"
```



