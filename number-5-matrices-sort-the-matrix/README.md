# #5 Matrices: Sort The Matrix

 - URL:[https://www.codewars.com/kata/590363d57e16c9b3c0000014](https://www.codewars.com/kata/590363d57e16c9b3c0000014)
 - Id: 590363d57e16c9b3c0000014
 - Language: python
 - Completed on: 2018-02-21T12:22:16.886Z
 - Tags: Algorithms,Matrix,Sorting,Data Structures,Fundamentals
 - Description:
You are given a matrix of `m rows` and `n columns` having integer numbers, positive an negative ones. You have to rearrenge it in order to have `all the rows sorted from left to right` and `all the columns sorted from top to bottom.`

E.g.:

Case 1: Square Matrix 3x3
```
matrix1 = [[7,  1,  4], 
           [3,  2,  8], 
           [6, -1, -6]] 
           
res1 =    [[-6, -1, 6], 
            [1,  3, 7], 
            [2,  4, 8]]  # having the required order
```

Case 2: Square Matrix 5x5
```
matrix2 = [[7,   1,   4,  2, -55], 
           [8,   2, -33,  1,   9], 
           [5,  61,  -9,  3,   8], 
           [2, -12,   9, 51,   6], 
           [4,   7,   2,  2,   1]]
           

res2 =   [[-55, 1, 2, 4,  7], 
          [-33, 1, 2, 4,  7], 
          [-12, 2, 2, 8,  9], 
          [ -9, 2, 5, 8, 51], 
          [  1, 3, 6, 9, 61]] # having the required order
```          
Case 3: Rectangle Matrix 5x3
```
matrix3 = [[7,  1,  4, 37, 28], 
           [3,  2,  8, 12, -8],
           [6, -1, -6,  7, 55]] 
           
res3 = [[-8, -1, 3,  7, 12], 
        [-6,  2, 6,  8, 37], 
        [ 1,  4, 7, 28, 55]]  # having the required order
```        
You will not be given a matrix with all the same elements

Features of the random tests for matrices mxn:
```
number of tests = 100
10 ≤ m ≤ 100
10 ≤ n ≤ 100
-10000 ≤ m[i,j] ≤ 10000
```

Enjoy it!
Only available for Python 2 by the moment.

Note: there are often different valid solutions. Use the algorithm you prefer, all that matters is that your answer fulfills the order requirement.









