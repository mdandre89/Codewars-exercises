# The Span Function

 - URL:[https://www.codewars.com/kata/54f2f335cb9d99e8530008d7](https://www.codewars.com/kata/54f2f335cb9d99e8530008d7)
 - Id: 54f2f335cb9d99e8530008d7
 - Language: javascript
 - Completed on: 2022-06-11T12:49:43.141Z
 - Tags: Functional Programming,Algorithms
 - Description:
The span function is a good one to know. It accepts an array and a predicate function and returns two arrays. The first array contains all the elements of the argument array up to the item that caused the first failure of the predicate. The second returned array contains the rest of the original array. The original array is not modified.

For example,

```javascript

function isEven (x) {
  return Math.abs(x) % 2 === 0;
}

var arr = [2,4,6,1,8,10];

// This is true
span(arr, isEven) === [[2,4,6],[1,8,10]]
```

Your task is to...wait for it... write your own span function!!!

Hint/Challenge: If you have completed [the takeWhile function](http://www.codewars.com/kata/the-takewhile-function) and [the dropWhile function](http://www.codewars.com/kata/the-dropwhile-function), then you can solve this problem in one line!
