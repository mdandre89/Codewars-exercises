# Knight vs King

 - URL:[https://www.codewars.com/kata/564e1d90c41a8423230000bc](https://www.codewars.com/kata/564e1d90c41a8423230000bc)
 - Id: 564e1d90c41a8423230000bc
 - Language: python
 - Completed on: 2022-06-28T16:59:56.983Z
 - Tags: Fundamentals
 - Description:
## Knight vs King

If you are not familiar with chess game you can learn more [Here](https://en.wikipedia.org/wiki/Chess) .

Here is the chess board (rows, denoted by numbers, are called *ranks*, columns, denoted by a letter, are called *files*):

![alt text](https://upload.wikimedia.org/wikipedia/commons/5/5b/Chess-board-with-letters_nevit_111.svg)

You put a Knight and a King in the board.

Complete the method that tell us which one can capture the other one.

You are provided with two object array; each contains an integer (the rank, first item) and a string/char (the file, second item) to show the position of the pieces in the chess board.

Return:
* `"Knight"` if the knight is putting the king in check,
* `"King"`   if the king is attacking the knight
* `"None"`   if none of the above occur

Example:
```
knight = [7, "B"], king = [6, "C"]  ---> "King"
```

Check the test cases and Happy coding :)
