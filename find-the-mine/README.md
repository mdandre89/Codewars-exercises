# Find the Mine!

 - URL:[https://www.codewars.com/kata/528d9adf0e03778b9e00067e](https://www.codewars.com/kata/528d9adf0e03778b9e00067e)
 - Id: 528d9adf0e03778b9e00067e
 - Language: python
 - Completed on: 2017-08-21T08:56:29.754Z
 - Tags: Arrays,Search,Algorithms
 - Description:
You've just discovered a square (NxN) field and you notice a warning sign. The sign states that there's a single bomb in the 2D grid-like field in front of you. 

Write a function `mineLocation`/`MineLocation` that accepts a 2D array, and returns the location of the mine. The mine is represented as the integer `1` in the 2D array. Areas in the 2D array that are not the mine will be represented as `0`s. 

The location returned should be an array (`Tuple<int, int>` in C#) where the first element is the row index, and the second element is the column index of the bomb location (both should be 0 based). All 2D arrays passed into your function will be square (NxN), and there will only be one mine in the array.

### Examples:
`mineLocation( [ [1, 0, 0], [0, 0, 0], [0, 0, 0] ] )` => returns `[0, 0]` <br/>
`mineLocation( [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ] )` => returns `[1, 1]` <br/>
`mineLocation( [ [0, 0, 0], [0, 0, 0], [0, 1, 0] ] )` => returns `[2, 1]`
