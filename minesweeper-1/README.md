# Minesweeper

 - URL:[https://www.codewars.com/kata/587b2ddb87264729e6000128](https://www.codewars.com/kata/587b2ddb87264729e6000128)
 - Id: 587b2ddb87264729e6000128
 - Language: python
 - Completed on: 2017-11-14T18:13:37.253Z
 - Tags: Algorithms,Puzzles
 - Description:
# Minesweeper

Write a program that adds the numbers to a minesweeper board

Minesweeper is a popular game where the user has to find the mines using
numeric hints that indicate how many mines are directly adjacent
(horizontally, vertically, diagonally) to a square.

In this exercise you have to create some code that counts the number of
mines adjacent to a square and transforms boards like this (where `*`
indicates a mine):

    +-----+
    | * * |
    |  *  |
    |  *  |
    |     |
    +-----+

into this:

    +-----+
    |1*3*1|
    |13*31|
    | 2*2 |
    | 111 |
    +-----+

``` python
inp = ["+------+",
       "| *  * |",
       "|  *   |",
       "|    * |",
       "|   * *|",
       "| *  * |",
       "|      |",
       "+------+"]

board(inp)

["+------+",
 "|1*22*1|",
 "|12*322|",
 "| 123*2|",
 "|112*4*|",
 "|1*22*2|",
 "|111111|",
 "+------+"]

```

Implementation note:

The board function must validate its input and raise a
ValueError/Error with a meaningfull error message if the
input turns out to be malformed.

