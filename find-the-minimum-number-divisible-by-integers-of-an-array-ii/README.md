# Find The  Minimum Number Divisible by Integers of an Array II

 - URL:[https://www.codewars.com/kata/56f1b3c94d0c330e4a000e95](https://www.codewars.com/kata/56f1b3c94d0c330e4a000e95)
 - Id: 56f1b3c94d0c330e4a000e95
 - Language: python
 - Completed on: 2017-10-12T11:24:24.663Z
 - Tags: Fundamentals,Mathematics,Optimization,Logic
 - Description:
Given a certain array of integers, create a function that may give the minimum number that may be divisible for all the numbers of the array.

This will be a harder version of ```Find The  Minimum Number Divisible by integers of an array I```

This is an example that shows how many times, a brute force algorithm cannot give a fast solution. We need the help of maths, in this case of number theory.

We need to apply the prime factorization of a number:

<a href="http://imgur.com/KYanmyW"><img src="http://i.imgur.com/KYanmyW.png?1" title="source: imgur.com" /></a>

Think in doing the prime factorization of the product of all the different values of the array and think how to obtain from it the minimum number that is divisible by all the values of the array.

See the same cases as the previous part:

```python
min_special_mult([2, 3 ,4 ,5, 6, 7]) == 420
```
The array may have integers that occurs more than once:
```python
min_special_mult([18, 22, 4, 3, 21, 6, 3]) == 2772
```
The array should have all its elements integer values. If the function finds an invalid entry (or invalid entries) like strings of the alphabet or symbols will not do the calculation and will compute and register them, outputting a message in singular or plural, depending on the number of invalid entries.

```python
min_special_mult([16, 15, 23, 'a', '&', '12']) == "There are 2 invalid entries: ['a', '&']"

min_special_mult([16, 15, 23, 'a', '&', '12', 'a']) == "There are 3 invalid entries: ['a', '&', 'a']"

min_special_mult([16, 15, 23, 'a', '12']) == "There is 1 invalid entry: a"
```
If the string is a valid number, the function will convert it as an integer.
```python
min_special_mult([16, 15, 23, '12']) == 5520

min_special_mult([16, 15, 23, '012']) == 5520
```
All the None elements of the array will be ignored:
```python
min_special_mult([18, 22, 4, , None, 3, 21, 6, 3]) == 2772
```
If the array has a negative number, the function will convert to a positive one.
```python
min_special_mult([18, 22, 4, , None, 3, -21, 6, 3]) == 2772

min_special_mult([16, 15, 23, '-012']) == 5520
```

The test for this part will be more challenging having arrays up to 5000 elements and up to 800 different values.

A simple brute force algorithm will not be able to pass the tests.
Enjoy it!



