# #9 Matrices: Adding diagonal products

 - URL:[https://www.codewars.com/kata/590bb735517888ae6b000012](https://www.codewars.com/kata/590bb735517888ae6b000012)
 - Id: 590bb735517888ae6b000012
 - Language: python
 - Completed on: 2022-06-23T15:35:56.179Z
 - Tags: Matrix,Algorithms,Fundamentals
 - Description:
We have a square matrix ```M``` of dimension ```n x n``` that has positive and negative numbers in the ranges ```[-9,-1]``` and ```[0,9]```,( the value ```0``` is excluded).

We want to add up all the products of the elements of the diagonals ```UP-LEFT to DOWN-BOTTOM```, that is the value of```sum1```; and the elements of the diagonals ```UP-RIGHT to LEFT-DOWN``` and that is ```sum2```. Then, as a final result, the value of ```sum1 - sum2```.

E.g.
```
M = [[ 1,  4, 7,  6,  5],
     [-3,  2, 8,  1,  3],
     [ 6,  2, 9,  7, -4],
     [ 1, -2, 4, -2,  6],
     [ 3,  2, 2, -4,  7]]
```     
Let's see how to get this result in the image below:

<a href="http://imgur.com/MHfydrP"><img src="http://i.imgur.com/MHfydrP.jpg?1" title="source: imgur.com" /></a>

So the value of ```sum1 - sum2``` is equal to:
```
1164 - 66 = 1098
```
Create the code to do this calculation.

Features of the random tests:
```
Numbers of tests = 150
5 <= dimension <= 25 (python, ruby and COBOL)
5 <= dimension <= 20 (javascript)
-10 < M[i,j] < 0 and 0 < M[i,j] < 10
```
This kata is available in Python2, Ruby and Javascript by the moment.
Translations into another languages will be released soon.
Enjoy it!
