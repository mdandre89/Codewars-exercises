# Flipping Game

 - URL:[https://www.codewars.com/kata/59841e5084533834d6000025](https://www.codewars.com/kata/59841e5084533834d6000025)
 - Id: 59841e5084533834d6000025
 - Language: python
 - Completed on: 2018-02-02T15:54:56.873Z
 - Tags: Algorithms,Games,Puzzles,Logic
 - Description:
Removed due to copyright infringement.

<!---

&ensp;Iahub got bored, so he invented a game to be played on paper.<br>
&ensp;He writes n integers a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>. Each of those integers can be either 0 or 1. He's allowed to do exactly one move: he chooses two indices i and j (1 ≤ i ≤ j ≤ n) and flips all values ak for which their positions are in range [i, j] (that is i ≤ k ≤ j). Flip the value of x means to apply operation x = 1 - x.<br>
&ensp;The goal of the game is that after exactly one move to obtain the maximum number of ones. Write a program to solve the little game of Iahub.
```
@param {Array} line of the input there are n integers: a1, a2, ..., an. 1 ≤ n ≤ 100. It is guaranteed that each of those n values is either 0 or 1
@return {Integer} the maximal number of 1s that can be obtained after exactly one move
```
Examples :
```
[1, 0, 0, 1, 0, 0]  =>  5
[1, 0, 0, 1]  =>  4

```
Note:<br>
&ensp;In the first case, flip the segment from 2 to 6 (i = 2, j = 6). That flip changes the sequence, it becomes: [1 1 1 0 1 1]. So, it contains four ones. There is no way to make the whole sequence equal to [1 1 1 1 1 1].<br>
&ensp;In the second case, flipping only the second and the third element (i = 2, j = 3) will turn all numbers into 1.

(c)ll931110 & fchirica

--->
