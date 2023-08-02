# Multisize Nonogram Encoder

 - URL:[https://www.codewars.com/kata/629049687438580064f0e6dd](https://www.codewars.com/kata/629049687438580064f0e6dd)
 - Id: 629049687438580064f0e6dd
 - Language: python
 - Completed on: 2022-06-27T13:02:22.205Z
 - Tags: Games,Algorithms
 - Description:
<h2>Nonogram encoder</h2>

If you're not familiar with nonograms, I recommend you to check this wikipedia page: <a href="https://en.wikipedia.org/wiki/Nonogram">Nonogram - Wikipedia</a>

My friend Alex really likes to solve nonograms, and I've drawn one for him:

<img src="https://i.imgur.com/IwaD1B6.png" width="400" height="400">

However, I'm too lazy to look through all 10 rows and all 10 columns to figure out all the clues.

Could you please write me a program that can convert a drawn nonogram (represented as tuple of tuples):

```
nonogram = (
  (0, 0, 0, 1, 0, 0, 0, 1, 1, 0),
  (0, 0, 1, 1, 1, 0, 1, 1, 1, 1),
  (0, 0, 1, 1, 1, 1, 1, 1, 1, 1),
  (0, 0, 0, 1, 1, 1, 1, 1, 1, 0),
  (0, 0, 0, 0, 0, 1, 1, 0, 0, 0),
  (0, 1, 0, 0, 0, 0, 1, 1, 0, 0),
  (1, 0, 1, 0, 0, 0, 1, 1, 0, 0),
  (1, 1, 1, 0, 0, 1, 1, 0, 0, 0),
  (1, 1, 1, 0, 0, 1, 1, 1, 0, 1),
  (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
)
```
Into a tuple of such structure:

`(column_clues, row_clues)`

where

`column_clues = ((4,), (1, 3), (2, 4),...)` and `row_clues = ((1, 2), (3, 4), (8,),...)`

Notes:
1. Any empty rows or empty columns (which are cosmically unlikely to occur in random tests) should be represented as an emply (zero-length) tuple 
2. Nonograms come in different sizes, such that `5 <= size <= 100`
3. There are 200 random tests

