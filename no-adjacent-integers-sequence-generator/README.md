# No adjacent integers sequence generator

 - URL:[https://www.codewars.com/kata/59a20f283203e8bd8c000006](https://www.codewars.com/kata/59a20f283203e8bd8c000006)
 - Id: 59a20f283203e8bd8c000006
 - Language: python
 - Completed on: 2017-09-08T11:17:35.769Z
 - Tags: Algorithms
 - Description:
Write a function that returns a list of all the integers from `lower` ( inclusive ) to `upper` ( exclusive ) in a such way that no two adjacent numbers in the list are numerically adjacent ( e.g. `5` cannot be next to `4` or `6` ).

The maximum sequence length tested is 10<sup>7</sup>. The minimum sequence length tested is _long enough._

#### Examples

For `solution(0,6)`: `5,0,4,1,3,2` would not be acceptable, because `3` and `2` are adjacent. `0,2,5,3,1,4` would be acceptable.
