# Diagonals

 - URL:[https://www.codewars.com/kata/5592dd43a9cd0e43a800019e](https://www.codewars.com/kata/5592dd43a9cd0e43a800019e)
 - Id: 5592dd43a9cd0e43a800019e
 - Language: python
 - Completed on: 2022-06-07T22:11:06.528Z
 - Tags: Matrix,Algorithms
 - Description:
Create a function that calculates all possible diagonals of a given (square) matrix.
Diagonals must be laid out from top to bottom


> Matrix = array of `n` length whose elements are `n` length arrays of integers.

2x2 example:

```javascript
diagonals( [
  [ 1, 2 ],
  [ 3, 4 ]
] ); 

returns -> [ [ 1 ], [ 2, 3 ], [ 4 ], [ 2 ], [ 1, 4 ], [ 3 ] ]

it is valid too -> [ [ 1, 4 ], [ 3 ], [ 2 ], [ 2 , 3 ], [ 1 ], [ 4 ] ] //Order of the returned array does not matter

it is invalid -> [ [ 1 ], [ 3, 2 ], [ 4 ], [ 2 ], [ 1, 4 ], [ 3 ] ] //Order of each diagonal must be preserved
```

3x3 example:

```javascript
diagonals( [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
] ); 

returns ->

[ [ 1 ],
  [ 2, 4 ],
  [ 3, 5, 7 ],
  [ 6, 8 ],
  [ 9 ],
  [ 3 ],
  [ 2, 6 ],
  [ 1, 5, 9 ],
  [ 4, 8 ],
  [ 7 ] ]
```

The tests verify that the implementation is efficient (1000x1000 matrix are used in tests).
