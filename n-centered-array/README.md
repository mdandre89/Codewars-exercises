# N-centered Array

 - URL:[https://www.codewars.com/kata/59b06d83cf33953dbb000010](https://www.codewars.com/kata/59b06d83cf33953dbb000010)
 - Id: 59b06d83cf33953dbb000010
 - Language: python
 - Completed on: 2017-09-18T14:27:22.345Z
 - Tags: Fundamentals
 - Description:
An array is called `centered-N` if some `consecutive sequence` of elements of the array sum to `N` and this sequence is preceded and followed by the same number of elements. 

Example:
```
[3,2,10,4,1,6,9] is centered-15
because the sequence 10,4,1 sums to 15 and the sequence 
is preceded by two elements [3,2] and followed by two elements [6,9]

```

Write a method called `isCenteredN` that returns :

- `true` if its array argument is `not empty` and `centered-N` or empty and centered-0
- otherwise returns `false`.
