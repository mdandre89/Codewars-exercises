# Game Hit the target

 - URL:[https://www.codewars.com/kata/5ffc226ce1666a002bf023d2](https://www.codewars.com/kata/5ffc226ce1666a002bf023d2)
 - Id: 5ffc226ce1666a002bf023d2
 - Language: python
 - Completed on: 2022-06-28T21:03:11.583Z
 - Tags: Games,Matrix,Arrays,Strings,Fundamentals
 - Description:
<h1>Hit the target</h1>
given a matrix <code>n x n</code> (2-7), determine if the arrow is directed to the target (x). <br>
There will be only 1 arrow '>' and 1 target 'x'<br>
An empty spot will be denoted by a space " ", the target with a cross "x", and the scope ">"
<h2>Examples:</h2>
given matrix 4x4: <br>
  <code>[<br>
  [' ', ' ', ' ', ' '],<br>
  [' ', ' ', ' ', ' '], --> return true<br>
  [' ', '>', ' ', 'x'],<br>
  [' ', ' ', ' ', ' ']<br>
] </code><br>
given matrix 4x4: <br>
  <code>[<br>
  [' ', ' ', ' ', ' '],<br>
  [' ', '>', ' ', ' '], --> return false<br>
  [' ', ' ', ' ', 'x'],<br>
  [' ', ' ', ' ', ' ']<br>
] </code><br>

given matrix 4x4: <br>
  <code>[<br>
  [' ', ' ', ' ', ' '],<br>
  [' ', 'x', '>', ' '], --> return false<br>
  [' ', '', ' ', ' '],<br>
  [' ', ' ', ' ', ' ']<br>
] </code>


In this example, only a 4x4 matrix was used, the problem will have matrices of dimensions from 2 to 7<br>
Happy hacking as they say!
