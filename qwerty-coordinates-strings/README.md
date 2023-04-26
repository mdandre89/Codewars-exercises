# Qwerty Coordinates -- Strings

 - URL:[https://www.codewars.com/kata/588b72fcd0c108ef8f00009d](https://www.codewars.com/kata/588b72fcd0c108ef8f00009d)
 - Id: 588b72fcd0c108ef8f00009d
 - Language: python
 - Completed on: 2017-10-13T10:18:46.850Z
 - Tags: Strings
 - Description:
Qwerty Coordinates -- Strings

A typical QWERTY keyboard layout is similar to this:
```
[Q][W][E][R][T][Y][U][I][O][P]
[A][S][D][F][G][H][J][K][L][;][']
[Z][X][C][V][B][N][M][,][.][?]
[ ][ ][   <Space>   ][ ][ ][ ]
```

(For this Kata, these are the only characters we're using)

Given a list of tuples of length two, where the tuple describes `(x, y)` on the keyboard, and where x and y start at 0, positioned at `[Q]`, and where `[<Space>]` occupies all coordinates from (2, 3) to (6, 3) inclusive, create the string as if it had been typed on this keyboard. Assume all letters are lowercase, except the first letter in the string, the first letter following a period or a question mark, and of course the letter "I" ('eye') by itself (no alpha characters before or after it). (Note on Question Mark -- there is no shift key in this kata, so assume all keys are their un-shifted variant, except [/] which should be [?], as shown in the diagram). Use provided test cases if necessary to determine exactly what qualifies as "by itself" for the letter I.

Hint: For capitalization, letters are alpha (a-z). If a letter should be capitalized following some punctuation, e.g. after a period, the first alpha character after that period should be capitalized. E.g. 'This., Is a test' is valid, 'This., is a test' is not. 

Examples:
```python
key_strokes([(5, 1), (2, 0), (8, 1), (8, 1), (8, 0), (7, 2), (5, 3), (1, 0), (8, 0), (3, 0), (8, 1), (2, 1)])
'Hello, world'
```

Other Constraints:

1) Aside from coordinates in the range representing spacebar, you will not receive any coordinates with a y value of 3.

2) All strings will start with an alpha character.

