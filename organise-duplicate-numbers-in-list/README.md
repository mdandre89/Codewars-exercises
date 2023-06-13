# Organise duplicate numbers in list

 - URL:[https://www.codewars.com/kata/5884b6550785f7c58f000047](https://www.codewars.com/kata/5884b6550785f7c58f000047)
 - Id: 5884b6550785f7c58f000047
 - Language: python
 - Completed on: 2017-03-13T15:52:47.771Z
 - Tags: Arrays,Sorting,Fundamentals
 - Description:
Sam is an avid collector of numbers. Every time he finds a new number he throws it on the top of his number-pile. Help Sam organise his collection so he can take it to the International Number Collectors Conference in Cologne. 

Given an array of numbers, your function should return an array of arrays, where each subarray contains all the duplicates of a particular number. Subarrays should be in the same order as the first occurence of the number they contain:
```javascript
group([3, 2, 6, 2, 1, 3])
>>> [[3, 3], [2, 2], [6], [1]]
```
Assume the input is always going to be an array of numbers. If the input is an empty array, an empty array should be returned.
