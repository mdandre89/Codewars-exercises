# Interlocking Binary Pairs

 - URL:[https://www.codewars.com/kata/628e3ee2e1daf90030239e8a](https://www.codewars.com/kata/628e3ee2e1daf90030239e8a)
 - Id: 628e3ee2e1daf90030239e8a
 - Language: python
 - Completed on: 2022-06-24T23:07:58.023Z
 - Tags: Binary,Bits,Algorithms
 - Description:
# Task

Write a function that checks if two non-negative integers make an "interlocking binary pair".

# Interlock ?
* numbers can be interlocked if their binary representations have no `1`'s in the same place
* comparisons are made by bit position, starting from right to left (see the examples below)
* when representations are of different lengths, the unmatched left-most bits are ignored

# Examples

1) `a = 9`, `b = 4`

Stacking representations shows how they can interlock. Here, no `1`'s share any position, so the function returns `true`.
   ```
    9    1001
    4     100
   ```

2) `a = 3`, `b = 6`

These representations do not interlock. Finding they both have a `1` in the same position, the function returns `false`.
   ```
    3      11
    6     110
   ```

# Input

Two non-negative integers in the range `0 <= n <= 2 ** 64 - 1`.

# Output

Boolean `true` or `false` whether or not these integers are interlockable.

# Enjoy!

Consider one of the following kata to solve next:
* [Crossword Puzzle! (2x2)](https://www.codewars.com/kata/5c658c2dd1574532507da30b)
* [Four Letter Words ~ Mutations](https://www.codewars.com/kata/5cb5eb1f03c3ff4778402099)
* [Is Sator Square?](https://www.codewars.com/kata/5cb7baa989b1c50014a53333)
* [Playing With Toy Blocks ~ Can you build a 4x4 square?](https://www.codewars.com/kata/5cab471da732b30018968071)
