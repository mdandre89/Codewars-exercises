# Simple Fun #223: Parameter Of Number

 - URL:[https://www.codewars.com/kata/5902f1839b8e720287000028](https://www.codewars.com/kata/5902f1839b8e720287000028)
 - Id: 5902f1839b8e720287000028
 - Language: python
 - Completed on: 2017-05-20T20:16:40.466Z
 - Tags: Puzzles
 - Description:
# Task
Let's define a `parameter` of number `n` as the least common multiple (LCM) of the sum of its digits and their product.

Calculate the parameter of the given number `n`.

# Input/Output

`[input]` integer `n`

 A positive integer. It is guaranteed that no zero appears in `n`.

`[output]` an integer

 The parameter of the given number.

# Example

For `n = 22`, the output should be `4`.

Both the sum and the product of digits equal 4, and LCM(4, 4) = 4.

For `n = 1234`, the output should be `120`.

`1+2+3+4=10` and `1*2*3*4=24`, LCM(10,24)=120

