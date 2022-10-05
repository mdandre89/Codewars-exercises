# Sum Times Tables

 - URL:[https://www.codewars.com/kata/551e51155ed5ab41450006e1](https://www.codewars.com/kata/551e51155ed5ab41450006e1)
 - Id: 551e51155ed5ab41450006e1
 - Language: python
 - Completed on: 2017-10-08T18:36:20.604Z
 - Tags: Fundamentals
 - Description:
Write a function `sumTimesTables` which sums the result of the sums of the elements specified in `tables` multiplied by all the numbers in between `min` and `max` including themselves.

For example, for `sumTimesTables([2,5],1,3)` the result should be the same as
```
2*1 + 2*2 + 2*3 +
5*1 + 5*2 + 5*3
```
i.e. the table of two from 1 to 3 plus the table of five from 1 to 3

All the numbers are integers but you must take in account:

* `tables` could be empty.
* `min` could be negative.
* `max` could be really big.
